import numpy as np
import numpy.linalg as nl

# menghitung jarak titik p3 dari garis yang dibentuk oleh titik p1 dan p2
def PointToLineDis(p1,p2,p3):
    p1 = np.asfarray(p1)
    p2 = np.asfarray(p2)
    p3 = np.asfarray(p3)
    d = nl.norm(np.cross(p2-p1, p1-p3))/nl.norm(p2-p1)
    return d

# mengurutkan list of point berdasarkan x kemudian y menaik
def sortPoints(list):
    return sorted(list , key=lambda x: [x[0], x[1]])

# mengurutkan list of point berdasarkan x kemudian y menurun
def sortPointsR(list):
    return sorted(list , key=lambda x: [x[0], x[1]], reverse=True)

# menghitung nilai determinan
def determinan(point, min_e, max_e):
    x1 = max_e[0] ; y1 = max_e[1] ; x2 = min_e[0] ; y2 = min_e[1] ; x3 = point[0] ; y3 = point[1]
    D = (x1*y2) + (x3*y1) + (x2*y3) - (x3*y2) - (x2*y1) - (x1*y3) 
    return D

#return list of outermost point untuk bagian kiri/atas
def DAC (list, min_e, max_e):       
    # basis
    if len(list) == 0:
        return []
    elif len(list) == 1 : 
        if PointToLineDis(min_e,max_e,list) == 0.0 :
            return []
        else : return list
    else : 
        max_distance = 0
        for point in list:
            d = PointToLineDis(min_e,max_e,point)
            if d > max_distance :
                max_distance = d
                new_max = point

        S1 = [] ; S2 = [] ; S = []

        for point in list :
            if determinan(point, min_e, new_max) < -0.1e-5 : 
                    S1.append(point)
            elif determinan(point,new_max,max_e) < -0.1e-5 :
                    S2.append(point)

        S.extend(DAC(S1,min_e,new_max))
        S.extend([new_max])                
        S.extend(DAC(S2,new_max,max_e))
        return S


#return list of outermost point untuk bagian kanan/bawah
def DAC2 (list, min_e, max_e):      
    # basis
    if len(list) == 0:
        return []
    elif len(list) == 1 : 
        if PointToLineDis(min_e,max_e,list) == 0.0 :
            return []
        else : return list
    else : 
        max_distance = 0
        for point in list:
            d = PointToLineDis(min_e,max_e,point)
            if d > max_distance :
                max_distance = d
                new_max = point

        S1 = [] ; S2 = [] ; S = []

        for point in list :
            if determinan(point, min_e, new_max) > 0.1e-5 :
                    S1.append(point)
            elif determinan(point,new_max,max_e) > 0.1e-5 :
                    S2.append(point)

        S.extend(DAC2(S1,min_e,new_max))
        S.extend([new_max])
        S.extend(DAC2(S2,new_max,max_e))
        
        return S

# main function
def myConvexHull (list):
    # urutkan list of point berdasarkan x kemudian y menaik
    list = sortPoints(list)
    # cari titik paling kiri/kanan, bagi dua bagian list 
    min_extreme = min(list, key=lambda x: [x[0], x[1]])
    max_extreme = max(list, key=lambda x: [x[0], x[1]])
    S1 = [] ; S2 = [] ; S = []
    for point in list :
            if determinan(point, min_extreme, max_extreme) > 0.1e-5 :
                    S2.append(point)
            elif determinan(point,min_extreme,max_extreme) < -0.1e-5 :
                    S1.append(point)
    # S berisi outermost point dengan urutan clockwise
    S.extend([min_extreme])
    S.extend(sortPoints(DAC(S1, min_extreme,max_extreme)))
    S.extend([max_extreme])
    S.extend(sortPointsR((DAC2(S2, min_extreme,max_extreme))))
    S.extend([min_extreme])
    return S
