1. isinstance(v_id, v_type)
 
	例如，判断一个变量是否为列表（list)

	isinstance(names, list)

2. 如何查找这些内置的方法（BIF）？
 
	输入 ： 

		dir(__builtins__)

	> 注意，builtins ，前后都是两个下划线

 
3. 上面只是一个列表，如何获得方法的详细信息

		help(bif_name)

	> 例如，help(isinstance)