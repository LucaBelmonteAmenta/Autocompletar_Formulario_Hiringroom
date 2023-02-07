# -*- encoding:utf-8 -*-
from Core import Core


class Main:

    @staticmethod
    def run():
        try:
            controlador = Core.loadModule("Controller")
            controlador.main()
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    Main.run()

    