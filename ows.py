# Get a subset coverage by slicing on time axis, trimming on spatial axes, and encoding result in image/jpeg.

from IPython.display import Image
import requests

# Set base url which can be used in further code examples
service_endpoint = "https://code-de.rasdaman.com/rasdaman/ows"
base_wcs_url = service_endpoint + "?service=WCS&version=2.0.1"

request = "&REQUEST=GetCoverage"
cov_id = "&COVERAGEID=S2_L2A_32631_TCI_60m"
subset_time = "&SUBSET=ansi(\"2017-04-03\")"
subset_e = "&SUBSET=E(640000,690000)"
subset_n = "&SUBSET=N(5090220,5115220)"
encode_format = "&FORMAT=image/jpeg"

response = requests.get(base_wcs_url + request + cov_id + subset_time + subset_e + subset_n + encode_format)

# Display result directly
Image(data=response.content)
