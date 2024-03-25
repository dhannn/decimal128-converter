**Analysis of the Implementation of the IEEE-754 Decimal-128 Floating-Point Converter**

The topic, IEEE-754 Decimal-128 floating-point converter, presents a challenge because of its increased precision compared to the usual Decimal32 and Decimal64 taught in class. At first, we needed to take into account to accurately handle numbers with more than 34 digits and the length of the field of a Decimal128 as well. To handle this, we needed to recall the IEEE-754 standard while applying the topic assigned to us.

Moving on to the coding implementation, our group adopted the Model-View-Controller (MVC) architecture, wherein the implementation process was divided into logic and GUI development. Initially, we focused on developing the core logic for the Decimal-128 converter, especially in translating decimal inputs into binary representation, considering rounding methods, and addressing special cases like NaN and infinity. It was a struggle at first to integrate the logic with the application, but the MVC architecture helped us to further incorporate it.

Lastly, testing our implementation presents a significant challenge to our group, specifically in handling edge cases required in the Decimal-128 precision. To fix this, we further documented and analyzed the potential edge cases using pen and paper, which assisted us in tracing it back to unit testing. We were able to recognize the importance of being detail-oriented during the whole implementation of the simulation project.

[Video demo of our project](https://youtu.be/91luqW7JkRM)
