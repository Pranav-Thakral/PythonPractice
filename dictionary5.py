country_capitals={"united states":"washington dc",
                  "italy":"rome",
                  "england":"london"}
def frame(**kwargs):
    for country in kwargs:
     print(country,kwargs[country])
frame(**country_capitals)