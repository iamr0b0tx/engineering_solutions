import json
from pprint import pprint
import math
import os


class WindTurbine:
    def __init__(self, site_data, t_data):
        super(WindTurbine, self).__init__()
        self.site_data = site_data

        self.t_data = t_data
        try:
            with open(os.path.abspath('../JSON files/wt_tip_speed_pow_coff.json')) as f:
                self.tip_speed_pow_coff = json.load(f)
        except FileNotFoundError:
            with open(os.path.abspath('./JSON files/wt_tip_speed_pow_coff.json')) as f:
                self.tip_speed_pow_coff = json.load(f)

    def analyse(self):
        density = self.site_data['air_data']['air_density']
        area = (math.pi * (self.t_data['blade_length'] ** 2))
        velocity = self.site_data['wind_dist_data']['velocity']

        tsr = (4 * math.pi) / self.t_data['no_blades']
        tsr_temp = str(round(tsr, 1))
        if int(tsr_temp[-1]) != 5:
            tsr = round(tsr, 0)
        p_coefficient = self.tip_speed_pow_coff[str(tsr)]

        power = p_coefficient * 0.5 * density * area * (velocity ** 3)
        print('P_Coefficient', p_coefficient)
        print('density', density)
        print('velocity', velocity)
        eff = self.t_data['rated_power'] / power * 100
        return {'power': power, 'efficiency': eff}


def wind_turbine_data(t_name, r_power, ci_wind_speed, co_wind_speed, r_diameter, h_height, units, b_length, no_blades):
    t_data = dict()
    t_data[t_name] = {}

    t_data[t_name]['rated_power'] = r_power
    t_data[t_name]['cut_in_wind_speed'] = ci_wind_speed
    t_data[t_name]['cut_out_wind_speed'] = co_wind_speed
    t_data[t_name]['rotor_diameter'] = r_diameter
    t_data[t_name]['hub_height'] = h_height
    t_data[t_name]['units'] = units
    t_data[t_name]['blade_length'] = b_length
    t_data[t_name]['no_blades'] = no_blades
    return t_data


def get_site_data(site_name, a_density, temp, altitude, pressure, w_shape_param, velocity, w_scale_param, height, lat, long):
    site_data = dict()
    site_data[site_name] = {}

    site_data[site_name]['air_data'] = {}
    site_data[site_name]['air_data']['air_density'] = a_density
    site_data[site_name]['air_data']['temp'] = temp     # oC
    site_data[site_name]['air_data']['altitude'] = altitude    # m
    site_data[site_name]['air_data']['pressure'] = pressure    #

    site_data[site_name]['wind_dist_data'] = {}
    site_data[site_name]['wind_dist_data']['w_shape_param'] = w_shape_param
    site_data[site_name]['wind_dist_data']['velocity'] = velocity
    site_data[site_name]['wind_dist_data']['w_scale_param'] = w_scale_param
    site_data[site_name]['wind_dist_data']['height'] = height

    site_data[site_name]['location'] = {}
    site_data[site_name]['location']['lat'] = lat
    site_data[site_name]['location']['long'] = long
    return site_data


if __name__ == '__main__':
    site_data = get_site_data('unilag', 1.2205, 27, 39, 4, 3.2, 4.3, 5.0, 10, 6.35, 3.20)
    t_data = wind_turbine_data('HITACHI TURBINE 104', 2000, 4, 25, 80, 70, 4, 39, 3)

    w_t = WindTurbine(site_data=site_data['unilag'], t_data=t_data['HITACHI TURBINE 104'])
    data = w_t.analyse()
    pprint(data)
