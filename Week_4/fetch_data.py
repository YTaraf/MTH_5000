import yfinance as yf
import pandas as pd

def get_weekly_data(
    ticker: str,
    start: str = None,
    end: str = None,
    auto_adjust: bool = True,
    keep_columns: list = None
) -> pd.DataFrame:
    """
    Fetch weekly historical stock data using yfinance.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol (e.g., "AMZN", "AAPL")
    start : str
        Start date in "YYYY-MM-DD"
    end : str
        End date in "YYYY-MM-DD" (default = today)
    auto_adjust : bool
        Whether to auto-adjust prices for splits/dividends
    keep_columns : list
        Optional list of columns to keep (e.g., ["Close", "Volume"])

    Returns
    -------
    pd.DataFrame
        Weekly stock data indexed by date
    """

    df = yf.download(
        ticker,
        start=start,
        end=end,
        interval="1wk",
        auto_adjust=auto_adjust,
        progress=False
    )

    # Clean empty result
    if df.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'")


    # Ensure index is datetime
    df.index = pd.to_datetime(df.index)

    return df