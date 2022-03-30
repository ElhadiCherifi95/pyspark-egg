import pytest

from helloworld.spark_provider import get_spark
from helloworld.transform import transform_column


class TestTransform(object):

    def test_with_transformed_col(self):
        # Given
        source_data = [
            ("Hello", 1),
            ("World", 2)
        ]
        source_df = get_spark().createDataFrame(
            source_data,
            ["word", "id"]
        )

        # When
        actual_df = transform_column(source_df)

        # Then
        expected_data = [
            ("Hello", 1, "Transformed !"),
            ("World", 2, "Transformed !")
        ]
        expected_df = get_spark().createDataFrame(
            expected_data,
            ["name", "age", "transformed_col"]
        )

        assert (expected_df.collect() == actual_df.collect())
