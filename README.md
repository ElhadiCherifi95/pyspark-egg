# Pyspark-egg

Sample pyspark project used to illustrate how to use eggs with pyspark REPL or with Spark Submit.

## How to use
### Generate egg
After sourcing the project you will be able to generate the egg file related to the project by calling:
`python setup.py bdist_egg`
The egg will be generated in `dist` directory of your project.

### With Spark REPL
Once the egg generated in `dist` directory, you can launch the pyspark REPL by specifying the egg like that:
`pyspark --py-files /path/to/your/project/dist/pyspark_hello_world_egg-0.0.1-py3.7.egg`

You can call now the associated code in your spark code:
`````
from helloworld.spark_provider import *
from helloworld.transform import transform_column

source_data = [("Hello", 1),("World", 2)]
source_df = get_spark().createDataFrame(source_data, ["word", "id"])

result_df = transform_column(source_df)
result_df.show()
`````
It should give you this output:
```
+-----+---+---------------+
| word| id|transformed_col|
+-----+---+---------------+
|Hello|  1|  Transformed !|
|World|  2|  Transformed !|
+-----+---+---------------+
```
### With Spark Submit
With spark submit it will be like that:
`
spark-submit --master local --py-files  /path/to/your/project/dist/pyspark_hello_world_egg-0.0.1-py3.7.egg
`
