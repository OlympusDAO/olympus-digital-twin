import numpy as np
def get_moving_standard_deviation_df(pdseries, windowlen = 30):
    mstd = pdseries.rolling(window=windowlen,min_periods=1).std()
    return mstd
def get_price_standard_deviation(df):
    # TODO: 1) seperate each run 2) calc the ma and then sd for each run 3) aggregate across runs...groups??
    av_std = []
    se_of_std = []
    for subset in df['subset'].unique():
        subset_std = []
        for run in df['run'].unique():
            subdf = df.loc[(df['subset']==subset) & (df['run']==run)]
            subset_std.append(np.nanmean(get_moving_standard_deviation_df(subdf['price'])))
        av_std.append(np.mean(subset_std))
        se_of_std.append(np.std(subset_std)/np.sqrt(len(subset_std)))
    return av_std,se_of_std