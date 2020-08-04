# SremmBot
A twitter bot that occasionally posts the Sremmlife 1 with increasing space between the two faces.

Included is a Python script designed to run the bot through the command line, which I'm still working to clean up and get fully function, along with a python notebook,
which works out of the box. This will only work if you have your own Twitter developer accound with authentication keys / access to the API
(I used tweepy, which made it super easy). For obvious security reasons my dev keys are not included in the repository
To get it working yourself, you need a file titled "auth_keys.py" which contains 4 string declarations for your developer API keys and the keys for your individual app.

The original picture was 950 x 950 pixels, which translated to 656kb. Sproutsocial claims:
"Maximum file size of 5 MB for photos, and 5 MB for animated GIFs on mobile and 15 MB on web." 
(https://sproutsocial.com/insights/social-media-image-sizes-guide/#twitter)

So, Either way, the bot should be able to run for a VERY long time before we reach the maximum file size, but as I accumulate more data about how the images grow on each iteration,
I should be able to come up with a rough estimate for when we will hit the max file size. I've only generated 3 iterations so far, and it appears as if the image grows about 1kb / iteration. So, if that pattern happens to persist, and the bot continually posts at a rate of 1 post / 3 hours,
Then a true 5MB limit should have the bot running for 543 days (or, 1.48 years!),
or 1793 days (4.91 years!) if the true limit is 15mb.
