

if __name__ == '__main__':
    from distributed import Client
    client = Client(n_workers=6)
    #import multiprocessing.popen_spawn_win32
    import modin.pandas as pd
    df = pd.read_csv("displaydata.csv",index_col=[0])

    print(df.head())
    