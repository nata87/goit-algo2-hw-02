from printer_3d_scheduler import test_printing_optimization
from rod_cutting_functions import run_tests
from colorama import init, Fore, Style
init(autoreset=True)

if __name__ == "__main__":
    print("\n" + Fore.CYAN  + "Результати задачі 1: Оптимізація 3D-друку")
    test_printing_optimization()
    print("\n" + Fore.CYAN  + "Результати задачі 2: Розрізання стрижня")
    run_tests()
