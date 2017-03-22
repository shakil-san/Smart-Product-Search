from ImportAmazonReviews import ImportAmazonReviews

x = ImportAmazonReviews()
assert isinstance(x.SearchAmazon, object)
x.SearchAmazon("Plant based protein powder")
