**为参数提供一个默认值，该参数就变成可选参数了。**

例如，定义这样一个参数
 
	def fun_a(required_arg, optional_arg = "I'm optionsl arg."):

调用时，可以这么调用：

	fun_a(arg0, arg1)

也可以这么调用：

	fun_a(arg0)