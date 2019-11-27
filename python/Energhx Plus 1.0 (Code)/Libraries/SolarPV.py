import json
from pprint import pprint


class SolarPV:
    stc = 25

    def __init__(self, insolation, constants, site_data, module_spec, inverter_spec):
        self.site_data = site_data
        self.inverter_spec = inverter_spec
        self.module_spec = module_spec
        self.insolation = insolation
        self.constants = constants

    def analyze(self):
        result = {}
        a_module = self.module_spec['mod_dim']['length'] * self.module_spec['mod_dim']['breadth']
        result['area'] = a_module

        n_pv_per_wing = round(self.site_data['area'] / a_module)
        result['no of pv modules per wing'] = n_pv_per_wing

        total_pv_mod = self.site_data['no_wings'] * n_pv_per_wing
        result['total no of pv modules'] = total_pv_mod

        installed_capacity = total_pv_mod * self.module_spec['rated power']
        result['installed capacity'] = installed_capacity

        f_temp = 1 - (self.constants['amb_temp'] * abs(self.module_spec['Temp Coeff']['temp_coeff_p']) / 100)
        result['f_temp'] = f_temp

        f_man = 1 - self.constants['tolerance']
        result['f_man'] = f_man

        f_dirt = 1 - self.constants['dirt_loss']
        result['f_dirt'] = f_dirt

        eff_inverter = self.inverter_spec['eff'] / 100
        result['eff inverter'] = eff_inverter

        eff_dc_cables = 1 - self.constants['assumed_dc_loss']
        result['eff dc cables'] = eff_dc_cables

        eff_ac_cables = 1 - self.constants['assumed_ac_loss']
        result['eff ac cables'] = eff_ac_cables

        sys_eff = f_temp * f_man * f_dirt * eff_inverter * eff_dc_cables * eff_ac_cables
        result['system efficiency'] = sys_eff

        actual_power = self.module_spec["rated power"] * sys_eff
        result['actual power'] = actual_power

        result_psh = {}
        for month in self.constants['months']:
            psh = self.insolation['21 deg'][month.lower()]
            result_psh[month] = psh
        result['psh'] = result_psh

        minimum_daily_pv = total_pv_mod * actual_power * psh / 1000
        result['min daily pv energy output'] = minimum_daily_pv

        psh_average = sum(list(self.insolation['21 deg'].values())) / float(len(self.insolation['21 deg']))
        result['average psh'] = psh_average

        annual_energy = total_pv_mod * actual_power * psh_average * 365
        result['annual energy'] = annual_energy

        specific_energy = annual_energy / installed_capacity
        result['specific energy'] = specific_energy

        performance_ratio = annual_energy / (installed_capacity * psh_average * 365)
        result['performance ratio'] = performance_ratio

        min_volt = self.module_spec['max_p_volt'] * (1 - self.constants['temp_effect'])
        result['min voltage'] = min_volt

        volt_inverter = min_volt * (1 - self.constants['assumed_dc_loss'])
        result['voltage inverter'] = volt_inverter

        min_number = round(
            (self.inverter_spec['mppt_volt_range_u'] * (1 + self.constants['safety_marg'])) / volt_inverter)
        result['min no of modules'] = min_number

        Voc = self.module_spec['open_c_vol'] + abs(SolarPV.stc - self.constants['eff_cell_temp']) * abs(
            self.module_spec['Temp Coeff']['temp_coeff_v'])
        result['v_oc'] = Voc

        max_num = int(self.inverter_spec['max_inp_volt'] / Voc)
        result['max no of modules'] = max_num

        return result


def get_site_data(loc, lat, long, elv, site, no_wings, area, pitch, install_type):
    data_dict = dict()
    data_dict[loc] = {}
    data_dict[loc]['latitude'] = lat
    data_dict[loc]['longitude'] = long
    data_dict[loc]['elevation'] = elv
    data_dict[loc]['site'] = site
    data_dict[loc]['no_wings'] = no_wings
    data_dict[loc]['area'] = area
    data_dict[loc]['pitch'] = pitch
    data_dict[loc]['installation_type'] = install_type
    return data_dict


def get_module_spec(name, r_power, max_p_volt, max_p_cur, open_c_vol, short_c_cur, op_temp_u, op_temp_l, max_sys_volt,
                    fuse_rating, pow_tol_u, pow_tol_l, temp_coeff_p, temp_coeff_v, temp_coeff_i, mod_eff, mod_dim, weight,
                    cell_type):
    data_dict = dict()
    data_dict[name] = {}
    data_dict[name]['rated power'] = r_power
    data_dict[name]['max_p_volt'] = max_p_volt
    data_dict[name]['max_p_cur'] = max_p_cur
    data_dict[name]['open_c_vol'] = open_c_vol
    data_dict[name]['short_c_cur'] = short_c_cur
    data_dict[name]['op_temp_u'] = op_temp_u
    data_dict[name]['op_temp_l'] = op_temp_l

    data_dict[name]['max_sys_volt'] = max_sys_volt
    data_dict[name]['fuse_rating'] = fuse_rating
    data_dict[name]['pow_tol_u'] = pow_tol_u
    data_dict[name]['pow_tol_l'] = pow_tol_l
    data_dict[name]['Temp Coeff'] = {}
    data_dict[name]['Temp Coeff']['temp_coeff_p'] = temp_coeff_p
    data_dict[name]['Temp Coeff']['temp_coeff_v'] = temp_coeff_v
    data_dict[name]['Temp Coeff']['temp_coeff_i'] = temp_coeff_i
    data_dict[name]['mod_eff'] = mod_eff
    data_dict[name]['mod_dim'] = mod_dim
    data_dict[name]['weight'] = weight
    data_dict[name]['cell_type'] = cell_type

    return data_dict


def get_inverter_spec(name, type, max_inp_volt, mppt_volt_range_u, mppt_volt_range_l, mppt_units, eff):
    data_dict = dict()
    data_dict[name] = {}
    data_dict[name]['type'] = type
    data_dict[name]['max_inp_volt'] = max_inp_volt
    data_dict[name]['mppt_volt_range_u'] = mppt_volt_range_u
    data_dict[name]['mppt_volt_range_l'] = mppt_volt_range_l
    data_dict[name]['mppt_units'] = mppt_units
    data_dict[name]['eff'] = eff

    return data_dict


if __name__ == '__main__':
    '''
    site_data = get_site_data('UNILAG', 6.52, 3.39, 45, 'roof of building', 88, 28.89, 21, 'Fixed Grid-Tied')

    module_spec = get_module_spec('ECLIPSAL NRG72 310M', 310, 36.78, 8.43, 45.12, 8.92, -40, 85, 1000, 15,
                                  0, 2, -0.484, -0.363, -0.047, 17,
                                  {'length': 1.983, 'breadth': 0.997, 'height': 0.042}, 25, 'mono-crystalline, 3 bus bar')

    inverter_spec = get_inverter_spec('TABUCHI ELECTRIC EPW-T250P6-US', 'three phase 25KW solar inverter', 1000,
                                      500, 800, 6, 98.5)

    spv = SolarPV(site_name='UNILAG', site_data=site_data, module_name='ECLIPSAL NRG72 310M', module_spec=module_spec,
                  inverter_name='TABUCHI ELECTRIC EPW-T250P6-US', inverter_spec=inverter_spec)
    '''
    insolatiown = {
        "0 deg": {"jan": 5.23, "feb": 5.43, "mar": 5.39, "apr": 5.13, "may": 4.68, "jun": 3.97, "jul": 3.88,
                      "aug": 3.92, "sept": 4.03, "oct": 4.5, "nov": 4.9, "dec": 5.12},
        "6 deg": {"jan": 5.45, "feb": 5.57, "mar": 5.43, "apr": 5.14, "may": 4.73, "jun": 4.02, "jul": 3.92,
                      "aug": 3.93, "sept": 4.03, "oct": 4.57, "nov": 5.07, "dec": 5.36},
        "21 deg": {"jan": 5.8, "feb": 5.72, "mar": 5.34, "apr": 4.0, "may": 4.71, "jun": 4.02, "jul": 3.91,
                       "aug": 3.85, "sept": 3.91, "oct": 4.59, "nov": 5.32, "dec": 5.77}
    }
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
    site_data = get_site_data('UNILAG', 6.52, 3.39, 45, 'roof of building', 88, 28.89, 21, 'Fixed Grid-Tied')

    module_spec = get_module_spec('ECLIPSAL NRG72 310M', 310, 36.78, 8.43, 45.12, 8.92, -40, 85, 1000, 15,
                                  0, 2, -0.484, -0.363, -0.047, 17,
                                  {'length': 1.983, 'breadth': 0.997, 'height': 0.042}, 25,
                                  'mono-crystalline, 3 bus bar')

    inverter_spec = get_inverter_spec('TABUCHI ELECTRIC EPW-T250P6-US', 'three phase 25KW solar inverter', 1000, 500, 800, 6, 98.5)

    constants = {'amb_temp': 30, 'tolerance': 0.05, 'dirt_loss': 0.05, 'assumed_dc_loss': 0.03, 'assumed_ac_loss': 0.01,
                 'months': months, 'temp_effect': 0.1, 'safety_marg': 0.1, 'eff_cell_temp': 15}
    spv = SolarPV(site_data=site_data['UNILAG'], module_spec=module_spec['ECLIPSAL NRG72 310M'], inverter_spec=inverter_spec['TABUCHI ELECTRIC EPW-T250P6-US'],  insolation=insolatiown, constants=constants)
    data_result = spv.analyze()

    pprint(data_result)
    with open('monthly_output.json', 'w') as f:
        f.write(json.dumps(data_result, indent=4, sort_keys=False))
