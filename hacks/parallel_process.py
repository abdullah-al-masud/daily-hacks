import concurrent.futures

class MultiProcessor():
    """
    Kind of base class for multi-processing
    """
    def __init__(self, num_workers=None, *args, **kwargs):
        self.num_workers = num_workers

    def run_for_all(self, iterator):
        with concurrent.futures.ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            results = executor.map(self.target_func, iterator)
        return [x for x in results]

    def target_func(self):
        pass


class FeatureProcessor(MultiProcessor):
    """
    Executing class
    """
    def __init__(self, data, feature_list, cfg):
        super(FeatureProcessor, self).__init__(max_workers=cfg.DATA.max_workers)
        self.data = data
        self.feature_list = feature_list
        self.cfg = cfg

    def target_func(self, tick):
        process_features(self.data, self.feature_list, tick, self.cfg)


def process_features(arg1, arg2):
    return arg1 + arg2


if __name__ == "__main__":

    """Dummy code to execute multi-processing"""
    d, f, cfg = None, None, None
    fp = FeatureProcessor(d, f, cfg)
    fp.run_for_all([1,2,3,4])