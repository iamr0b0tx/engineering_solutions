from pprint import pprint


class CoolingLoad:
    ballast_factor = 1.2
    clf = 1
    heat_gained_based_on_people = {
        'moderately active work (office)': {'sensible': 75, 'latent': 55},
        'standing, light work, or walking (store)': {'sensible': 75, 'latent': 55},
        'light bench work (factory)': {'sensible': 80, 'latent': 140},
        'heavy work (factory)': {'sensible': 170, 'latent': 225},
        'athletics (gymnasium)': {'sensible': 210, 'latent': 315}
    }

    def __init__(self, space_dict, constant, appliance):
        self.space_dict = space_dict
        self.constants = constant
        self.appliances = appliance

    def analysis(self):
        overall_ht = dict()
        r_total = 0
        for th_input in self.constants['th_walls']:
            try:
                r_total += self.constants['th_walls'][th_input]['length'] / self.constants['th_walls'][th_input]['conductivity']
            except KeyError:
                r_total += self.constants['th_walls'][th_input]['conductivity']

        overall_ht['walls'] = {}
        overall_ht['walls']['u_factor'] = 1 / r_total

        r_total = 0
        for th_input in self.constants['th_roof']:
            try:
                r_total += self.constants['th_roof'][th_input]['length'] / self.constants['th_roof'][th_input]['conductivity']
            except KeyError:
                r_total += self.constants['th_roof'][th_input]['conductivity']

        overall_ht['roof'] = {}
        overall_ht['roof']['u_factor'] = 1 / r_total

        overall_ht['glass'] = {}
        overall_ht['glass']['u_factor'] = self.constants['th_glass']

        final_result = dict()
        for heat_inlet in overall_ht:
            heat_gained = dict()
            total = 0
            for cardinal in self.space_dict['heat_gained'][heat_inlet]:
                heat_gained[cardinal] = {}
                heat_gained[cardinal]['u_factor'] = overall_ht[heat_inlet]['u_factor']
                heat_gained[cardinal]['area'] = self.space_dict['heat_gained'][heat_inlet][cardinal]
                heat_gained[cardinal]['dT'] = abs(self.space_dict['weather']['indoor']['dry_bulb'] -
                                                  self.space_dict['weather']['outdoor']['dry_bulb'])
                try:
                    heat_gained[cardinal]['cltd'] = self.constants['cltd'][heat_inlet][cardinal]
                except TypeError:
                    heat_gained[cardinal]['cltd'] = self.constants['cltd'][heat_inlet]
                heat_gained[cardinal]['cardinal_total_heat'] = heat_gained[cardinal]['u_factor'] * \
                                                               heat_gained[cardinal]['area'] * heat_gained[cardinal][
                                                                   'cltd']

                total += heat_gained[cardinal]['cardinal_total_heat']

            heat_gained['total'] = total
            final_result[heat_inlet + '_conduction'] = heat_gained

        final_result['glass_radiation'] = {}
        total = 0
        for cardinal in self.space_dict['heat_gained']['glass']:
            final_result['glass_radiation'][cardinal] = {}
            final_result['glass_radiation'][cardinal]['area'] = self.space_dict['heat_gained']['glass'][cardinal]
            final_result['glass_radiation'][cardinal]['sc'] = self.constants['sc'][cardinal]
            final_result['glass_radiation'][cardinal]['scl'] = self.constants['scl'][cardinal]

            final_result['glass_radiation'][cardinal]['cardinal_total_heat'] = final_result['glass_radiation'][cardinal]['area'] * final_result['glass_radiation'][cardinal]['sc'] * final_result['glass_radiation'][cardinal]['scl']

            total += final_result['glass_radiation'][cardinal]['cardinal_total_heat']

        final_result['glass_radiation']['total'] = total

        total_heat_appliances = 0
        for appliance in self.appliances:
            ballast_factor = 1
            if 'Fluorescent' in appliance:
                ballast_factor = 1.2
            total_heat_appliances += (self.appliances[appliance]['units'] * self.appliances[appliance]['power_rating'] * ballast_factor * CoolingLoad.clf)
        final_result['heat_appliances'] = {'total': total_heat_appliances}

        final_result['heat_people'] = {'Q_sensible': 0, 'Q_latent': 0}

        level_activity = self.space_dict['level_activity'].lower()
        people_q_sensible = CoolingLoad.clf * CoolingLoad.heat_gained_based_on_people[level_activity]['sensible'] * sum(self.space_dict['heat_gained']['people'].values())
        people_q_latent = CoolingLoad.clf * CoolingLoad.heat_gained_based_on_people[level_activity]['latent'] * sum(self.space_dict['heat_gained']['people'].values())
        final_result['heat_people']['Q_sensible'] = people_q_sensible
        final_result['heat_people']['Q_latent'] = people_q_latent
        final_result['heat_people']['total'] = people_q_sensible + people_q_latent

        volume = self.space_dict['heat_gained']['height']

        airflow = (volume * self.space_dict['heat_gained']['infiltration_rate'] / 3600)
        temp_diff = abs(self.space_dict['weather']['indoor']['dry_bulb'] - self.space_dict['weather']['outdoor']['dry_bulb'])
        hum_diff = abs(self.space_dict['weather']['indoor']['humidity'] - self.space_dict['weather']['outdoor']['humidity'])

        final_result['heat_infiltration'] = {}
        infiltration_q_sensible = 1210 * airflow * temp_diff
        infiltration_q_latent = 3010 * airflow * hum_diff

        final_result['heat_infiltration']['Q_sensible'] = infiltration_q_sensible
        final_result['heat_infiltration']['Q_latent'] = infiltration_q_latent
        final_result['heat_infiltration']['total'] = infiltration_q_sensible + infiltration_q_latent

        ventilation_air_flow = {
            'auditorium': 0.008,
            'class room': 0.008,
            'locker room': 0.0025,
            'office space': 0.01,
            'public restroom': 0.025,
            'smoking lounge': 0.03
        }
        final_result['heat_ventilation'] = {}
        ventilation_q_sensible = 1210 * ventilation_air_flow[self.space_dict['type_space'].lower()] * temp_diff
        ventilation_q_latent = 1210 * ventilation_air_flow[self.space_dict['type_space'].lower()] * hum_diff

        final_result['heat_ventilation']['Q_sensible'] = ventilation_q_sensible
        final_result['heat_ventilation']['Q_latent'] = ventilation_q_latent
        final_result['heat_ventilation']['total'] = ventilation_q_sensible + ventilation_q_latent

        return final_result


def create_space_dict(name, room_area, weather_in_dry, weather_in_hum, weather_out_dry, weather_out_hum, level_activity,
                      type_space, heat_gained):
    data_dict = dict()
    data_dict[name] = {}
    data_dict[name]['room_area'] = room_area
    data_dict[name]['weather'] = {}
    data_dict[name]['weather']['indoor'] = {'dry_bulb': weather_in_dry, 'humidity': weather_in_hum}
    data_dict[name]['weather']['outdoor'] = {'dry_bulb': weather_out_dry, 'humidity': weather_out_hum}
    data_dict[name]['level_activity'] = level_activity
    data_dict[name]['type_space'] = type_space
    data_dict[name]['heat_gained'] = heat_gained
    return data_dict


def create_multiple_key_value(**kwargs):
    return kwargs


if __name__ == '__main__':
    h_gained = dict()
    h_gained['people'] = {'men': 90, 'women': 5}
    h_gained['glass'] = {'north': 69.54, 'south': 60.3, 'east': 45.23, 'west': 39.45}
    h_gained['walls'] = {'north': 90.25, 'south': 56.23, 'east': 93.32, 'west': 42.52}
    h_gained['roof'] = {'floor_area': 210.45}
    h_gained['infiltration_rate'] = 0.3
    h_gained['height'] = 20

    new_app = {
        'Laptop': {"power_rating": 3, "units": 2, "operating_hours": 5},
        'Printer': {"power_rating": 34, "units": 12, "operating_hours": 10},
        'Lightning (Fluorescent)': {"power_rating": 34, "units": 12, "operating_hours": 10, 'Fluorescent': True},
        'Lightning (Others)': {"power_rating": 34, "units": 12, "operating_hours": 10},
        'Incandacent Light': {"power_rating": 34, "units": 12, "operating_hours": 10}
    }

    space_dict = create_space_dict(name='R271', room_area=6, weather_in_dry=92.50, weather_in_hum=122, type_space='Class room',
                                   weather_out_dry=78, weather_out_hum=78, level_activity='Moderately active Work (Office)',
                                   heat_gained=h_gained)

    th_input_wall = dict()
    th_input_wall['concrete'] = create_multiple_key_value(length=0.2, conductivity=1.73)
    th_input_wall['plaster_in'] = create_multiple_key_value(length=0.0125, conductivity=8.65)
    th_input_wall['plaster_out'] = create_multiple_key_value(length=0.0125, conductivity=8.65)
    th_input_wall['outside_film'] = create_multiple_key_value(conductivity=0.04)
    th_input_wall['inside_film'] = create_multiple_key_value(conductivity=0.12)

    th_input_roof = dict()
    th_input_roof['concrete'] = create_multiple_key_value(length=0.2, conductivity=1.73)
    th_input_roof['plaster'] = create_multiple_key_value(length=0.0125, conductivity=8.65)
    th_input_roof['outside_film'] = create_multiple_key_value(length=1, conductivity=6.3)
    th_input_roof['inside_film'] = create_multiple_key_value(length=1, conductivity=9.4)

    th_glass = 6.12

    cltd_input1 = {
        'walls': {'north': 3, 'east': 3, 'south': 42.7, 'west': 42.7},
        'glass': {'north': 7, 'east': 7, 'south': 7, 'west': 7},
        'roof': 30.83
    }

    scl_input1 = {'north': 15.76, 'east': 15.76, 'south': 5.51, 'west': 46.07}
    sc_input1 = {'north': 0.82, 'east': 0.82, 'south': 0.82, 'west': 0.82}

    constants = {
        'th_walls': th_input_wall,
        'th_roof': th_input_roof,
        'th_glass': th_glass,
        'scl': scl_input1,
        'sc': sc_input1,
        'cltd': cltd_input1
    }

    c_load = CoolingLoad(space_dict=space_dict['R271'], constant=constants, appliance=new_app)
    result = c_load.analysis()
    pprint(result)
