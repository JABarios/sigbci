import pathlib
import os
import os.path
import configparser


def lista_registros(mipath, miglob):
    # lista_registros("/home/juan/pro","*.py") funciona
    desktop = pathlib.Path(mipath)
    xx = desktop.rglob(miglob)
    return list(xx)


def archivo_registros(lista_arch, mipath, archivo):
    arch_csv = os.path.join(".", "out", mipath, archivo)
    # open file in write mode
    print(arch_csv)
    with open(arch_csv, "w") as fp:
        for item in lista_arch:
            # write each item on a new line
            fp.write("%s\n" % item)
    print("Done")


def read_ini(seccion, variable):
    config_file = os.path.join(os.path.expanduser("~"), ".sigbci")
    config = configparser.ConfigParser()
    config.read(config_file)
    # for section in config.sections():
    #    for key in config[section]:
    #        print((key, config[section][key]))
    return config[seccion][variable]


def get_registro(ini_var, num_orden):
    archivos = lista_registros(read_ini("DIR", ini_var), "*.dat")
    return archivos[num_orden]
