# -*- coding: utf-8 -*-

# this code can compute the BMI to text people health


print('请输入身高/m')
height = float(input())
print('请输入体重/kg')
weight = float(input())

num_BMI = weight/height/height

if num_BMI < 18.5:
    print('BMI值为',num_BMI,'体型过轻')
elif num_BMI < 25:
    print('BMI值为',num_BMI,'体型正常')
elif num_BMI < 28:
    print('BMI值为',num_BMI,'体型过重')
elif num_BMI < 32:
    print('BMI值为',num_BMI,'体型肥胖')
else:
    print('BMI值为',num_BMI,'体型严重肥胖')

