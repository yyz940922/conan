    test_processed_profile
        self.assertIn("patch: error: no patch data found!", client.out)
        ret = loader.load_consumer(file_path, test_processed_profile())