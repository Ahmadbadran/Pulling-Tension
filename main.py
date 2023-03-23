import math


class Main:
    @staticmethod
    def main(args):

        straightCase = 0.0
        cof = 0.0
        w = 0.0
        T0 = 0.0
        T = 0.0
        r = 0.0
        theta = 0.0
        x = 0.0
        h = 0.0
        OdOFCable = 0.0
        IDOfDuct = 0.0
        MAxTensionOfPulledItem = 0.0

        # entering common variables like
        # waight, od of cable,idOfDuct,MAxTensionOfPulledItem,Cof,
        print("please enter these comman variables ")
        print("waight = ")
        w = float(input())
        print("The Outside Diameter OF Cable = ")
        OdOFCable = float(input())
        print("The Inside Diameter Of duct = ")
        IDOfDuct = float(input())
        print("The Co-Efficient-of-Friction")
        cof = float(input())
        print("The Max Tension Of Pulled Item")
        MAxTensionOfPulledItem = float(input())
        DFR = OdOFCable / IDOfDuct * 100
        print("DFR = " + str(DFR) + "%")
        if DFR < 80:
            print("Accepted Range Of DFR")
        else:
            print("Please consulte the technical team ")

        print("if you want to pull Duct enter 1 ,Cable enter 2")
        choose = input()

        print("Is the existing duct empty enter 1 , occupied enter 2")
        choose = input()
        if int(choose) == 2:
            print("the occupied equations are not ready yet!")
        elif int(choose) == 1:

            while True:
                print("please choose if you want to calculate the tension of straight line press 1 , curve press 2")
                choose = input()
                if int(choose) == 1:

                    print(
                        "please enter 0 to calculate straight line \n1 to calculate inclined line \n 2 to calculate declined line .")
                    straightCase = float(input())
                    if int(straightCase) == 0:
                        print("please enter your values in lbf ")
                        if T == 0:
                            print("enter the back tension: ")
                            T0 = float(input())
                        else:
                            T0 = T

                        print("enter the Section Length: ")
                        distance = float(input())
                        T = T0 + cof * w * distance

                        print("the total tension in bound  = " + str(T) + " lbf")
                        print("the total tension in newten = " + str(T * 4.45) + "N")

                    elif int(straightCase) == 1:
                        print("please enter your values in lbf ")
                        if T == 0:
                            print("enter the back tension: ")
                            T0 = float(input())
                        else:
                            T0 = T

                        print("enter the horizantal projection of segment x")
                        x = float(input())
                        print("enter the vertical projection od segment h")
                        h = float(input())
                        T = T0 + w * (cof * x + h)

                        print("the total tension in bound  = " + str(T) + " lbf")
                        print("the total tension in newton = " + str(T * 4.45) + "N")

                    elif int(straightCase) == 2:
                        print("please enter your values in lbf ")
                        if T == 0:
                            print("enter the back tension: ")
                            T0 = float(input())
                        else:
                            T0 = T

                            print("enter the horizantal projection of segment x")
                            x = float(input())
                            print("enter the vertical projection of segment h")
                            h = float(input())
                            T = T0 + w * (cof * x - h)
                            print("the total tension in bound  = " + str(T) + " lbf")
                            print("the total tension in newton = " + str(T * 4.45) + "N")

                elif int(choose) == 2:
                    print("please enter the value of r")
                    r = float(input())
                    print("please enter the value of theta")
                    theta = float(input())
                    if T == 0:
                        print("enter the back tension: ")
                        T0 = float(input())
                    else:
                        T0 = T
                    # T = btension * Math.cosh(f*theta)+(Math.sinh(f*theta)*Math.sqrt((btension*btension)+((w*r)*(w*r)))) ;
                    T = w * r * (math.sinh(math.asinh(T0 / (w * r)) + (cof * theta / 57.3)))

                    print("tension by the equation in bound  = " + str(T) + " lbf")
                    print("tension by the equation in newton = " + str(T * 4.45) + "N")



                else:
                    print("please enter a valid value.")

                if input('Do You Want To Continue? (y/n)') != 'y':
                    print('the total Tension = ' + str(T))
                    if T < MAxTensionOfPulledItem:
                        print("You can install your cable ")
                    else:
                        print("Please Consulte the technical Team! For Solution")
                    break


if __name__ == "__main__":
    Main.main([])

