import numpy as np

class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006,
                       2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955,
                       1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966,
                       1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965,
                       1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955,
                       1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994,
                       1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975,
                       1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015,
                       2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966,
                       1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])

patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

class_year_median = np.array([4,6,8,10,7,5])

millennials = np.mean(class_year >= 2005)   #calculates the percentage of people graduating in 2005 or after
print(millennials)
print(len(class_year))

class_year_median = np.median(class_year)
print(class_year_median)

thirtieth_percentile = np.percentile(patrons, 30)
print(thirtieth_percentile)


