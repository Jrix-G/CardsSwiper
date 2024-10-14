import math

def coord_centre_cercle(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

def coord_bas_losange(x1, y1, x2, y2):
    x = x2
    y = y1 - (y2 - y1)
    return x, y

def coordDEF():
    xA = float(input("Enter the x-coordinate of point A"))
    yA = float(input("Enter the y-coordinate of point A"))
    xB = float(input("Enter the x-coordinate of point B"))
    yB = float(input("Enter the y-coordinate of point B"))
    xC = float(input("Enter the x-coordinate of point C"))
    yC = float(input("Enter the y-coordinate of point C"))
    
    xD = (xA + xB) / 2
    yD = (yA + yB) / 2
    xE = xB
    yE = yA - (yB - yA)
    xF = (xE + xC) / 2
    yF = (yE + yC) / 2
    
    return xD, yD, xE, yE, xF, yF

def volume_sphere(r=1):
    return (4 / 3) * math.pi * r**3

def volume_cone(h, r=1):
    return (math.pi * r**2 * h) / 3

def volume_figure():
    r1 = float(input("Enter the radius of the left sphere"))
    r2 = float(input("Enter the radius of the middle sphere"))
    r3 = float(input("Enter the radius of the right sphere"))
    r_cone = float(input("Enter the radius of the cone"))
    h_cone = float(input("Enter the height of the cone"))
    h_above_cone = float(input("Enter the height of the above cone"))

    volume = (volume_sphere(r1) + volume_sphere(r2) + volume_sphere(r3) + volume_cone(h_cone, r_cone))
    volume_above_cone = math.pi * r_cone**2 * h_above_cone
    volume += volume_above_cone
    return volume

if __name__ == "__main__": # NE PAS SUPPRIMER CETTE LIGNE
    print("Debut du prog. principal")


