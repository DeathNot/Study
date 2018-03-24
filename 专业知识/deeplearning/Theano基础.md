# 符号变量
Theano有其独立的变量体系，Theano的变量类型称为符号变量，记为`TensorVariable`，它是Theano表达式和运算操作的基本单元。Theano创建符号变量的方式主要有以下几种：

  1. 使用内置的变量类型创建

      Theano当前支持七种内置的变量类型，分别是`scalar`，`vector`，`row`，`col`，`matrix`，`tensor3`，`tensor4`。
      ```python
      import theano 
      import theano.tensor as T
      data = T.vector(name='data', dtype='float32')
      ```
      Theano变量支持的数据类型包括八种，`int8`，`int16`，`int32`，`int64`，`float32`，`float64`，`complex64`，`complex128`。

    2. 自定义变量类型

        Theano提供了`TensorType`方法来自定义数据类型。
        ```python
        import theano
        import theano.tensor as T
        mytype = T.TensorType(dtype, broadcastable, name=None, sparse_grad=False)
        ```
        其中`dtype`和`broadcastable`是必须指定的，也是最常用的参数。
          * dtype：指定变量的类型
          * broadcastable：是一个由true或false值构成的布尔类型数组，元组的大小等于变量的维度大小。
