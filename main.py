from img2dataset import download

if __name__ == "__main__":
    download(
        url_list=r"/mnt/c/Users/smartmind/Desktop/workspace/test/laion2b_korean.parquet",
        image_size=256,
        output_folder="output",
        processes_count=8,
        resize_mode="keep_ratio",
        resize_only_if_bigger=True,
        encode_quality=100,
        encode_format="webp",
        output_format="parquet",
        input_format="parquet",
        url_col="URL",
        caption_col="TEXT",
        save_additional_columns=["similarity"],
        distributor="pyspark",
        retries=1,
    )
