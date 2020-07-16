"""
13.Петя перешел в другую школу. На уроке физкультуры ему понадобилось
определить своё место в строю. Помогите ему это сделать.(input: 165,
163, 160, 160, 157, 157, 155, 154 input2: 162 output: 3 )
"""
# 165,163, 160, 160, 157, 157, 155, 154 
# input2: 162
#  output: 3

list_ = [165,163, 160, 160, 157, 157, 155, 154 ]
petya = 162

list_.insert(2,162)
for lydi in enumerate(list_,1):

    enumerate_,lydi_s_rostom = lydi

    if enumerate_ == 3:
        
        print(enumerate_)




