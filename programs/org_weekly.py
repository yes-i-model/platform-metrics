import pandas as pd
import numpy as np

fileinput = str(input("Which file do you want? "))
if not ".csv" in fileinput:
  fileinput += ".csv"

l1 = [1005, 1034, 1038, 1390, 1391, 2406, 2407, 2425, 2455, 2456, 2457, 2458, 2459, 2461, 2832, 2834, 3940, 3439, 6122, 6121, 5627, 73, 118, 242, 287, 289, 291, 292, 293, 294, 296, 299, 300, 302, 303, 304, 305, 306, 307, 308, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 467, 969, 1001, 4302, 2181, 2298, 2299, 2300, 2301, 2920, 2921, 3373, 3374, 4062, 4133, 4301, 4303, 4496, 5751, 2177, 2178, 2179, 2180, 1740, 1511, 1510, 827, 648, 499, 254, 252, 251, 249, 248, 247, 246, 169, 118, 118, 5223, 5222, 5221, 5220, 5219, 5218, 5216, 5215, 2176, 5227, 4831, 4750, 3946, 3945, 5228, 4878, 175, 191, 1749, 2073, 2074, 2075, 2076, 3944, 2121, 3325, 3621, 3943, 2077, 2078, 2106, 6098, 5995, 5876, 5862, 5860, 5859, 5858, 5709, 5667, 5613, 5538, 5537, 5535, 5534, 5533, 5532, 5531, 5530, 5529, 525, 1964, 4758, 4758, 4757, 4728, 333, 6347, 5773, 5754, 4911, 4910, 4909, 4908, 4907, 4906, 4905, 4804, 4757, 4728, 4727, 4546, 3454, 2815, 2593, 333, 6347, 6192, 5773, 4804, 5598, 5599, 5600, 5859, 3504, 648, 816, 817, 818, 820, 821, 822, 823, 824, 825, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 838, 1008, 1098, 1586, 1754, 263, 2000, 2166, 2167, 2168, 2169, 2170, 2171, 2177, 2197, 2357, 2738, 2746, 2831, 2832, 2836, 2920, 2921, 2923, 2924, 2944, 3156, 3293, 3410, 3411, 3412, 3413, 3414, 3415, 3416, 3750, 3751, 3794, 3985, 4390, 4487, 4667, 4692, 4699, 4709, 5026, 5027, 5028, 5088, 5101, 5561, 6094, 1782, 282, 539, 541, 553, 80, 118, 249, 2425, 4367, 4368, 4369, 4370, 4371, 4372, 4373, 4374, 4746, 5384, 6121, 6122, 2831, 282, 462, 467, 562, 572, 840, 947, 981, 997, 1141, 3715, 2832, 2833, 3156, 1663, 2234, 3714, 3713, 3712, 3711, 3717, 3815, 3940, 5508, 5505, 4982, 4797, 4377, 4343, 4069, 3621, 3185, 2930, 2711, 2596, 173, 388, 738, 740, 1109, 1529, 1632, 1966, 2017, 2019, 2110, 2210, 2356, 6098, 5956, 5955, 5954, 5953, 5952, 5951, 5950, 5949, 5948, 5947, 5946, 5945, 5944, 5943, 5942, 5941, 5940, 5939, 5938, 5937, 5936, 5935, 5934, 5933, 5917, 5916, 5915, 5914, 5913, 5912, 5911, 5910, 5909, 5908, 5907, 5906, 5905, 5904, 5903, 5902, 5901, 5900, 5899, 5898, 5897, 5896, 5876, 5875, 5874, 5873, 5872, 5871, 5870, 5869, 5868, 5867, 5866, 5862, 5859, 5858, 5709, 5682, 5667, 5527, 5526, 5525, 5524, 5523, 5522, 5521, 5520, 5519, 5518, 5517, 5516, 5515, 5514, 5513, 5512, 5511, 5510, 5509, 5506, 5337, 4961, 4878, 4662, 4102, 3666, 3196, 3195, 3194, 3193, 3192, 3191, 3190, 3189, 3188, 3187, 3186, 3184, 2567, 2028, 1908, 1002, 850, 616, 556, 180, 173, 6076, 6075, 6074, 6073, 6072, 6071, 6070, 6069, 6068, 6067, 6066, 6065, 6064, 6063, 6062, 6061, 6060, 6059, 6058, 6057, 6056, 6055, 6054, 6053, 6052, 6051, 6050, 6049, 6048, 6047, 6046, 6045, 6044, 6043, 6042, 6041, 6040, 6039, 6038, 6037, 6036, 6035, 6034, 6033, 6032, 6031, 6030, 6029, 6028, 6027, 6026, 6025, 6024, 6023, 6022, 6021, 6020, 6019, 6018, 6017, 6016, 6015, 6014, 6013, 6012, 6011, 6010, 6009, 6008, 6007, 6006, 6005, 6004, 6003, 6002, 6001, 6000, 5999, 5998, 5997, 5996, 5995, 5994, 5993, 5992, 5991, 5990, 5989, 5988, 5987, 5986, 5985, 5984, 5983, 5982, 5981, 5980, 5979, 5978, 5977, 5976, 5975, 5974, 5973, 5972, 5971, 5970, 5969, 5968, 5967, 5966, 5965, 5964, 5862, 5704, 5701, 5599, 5507, 4416, 4791, 4790, 4599, 4491, 4481, 4480, 4479, 4478, 4477, 4476, 4475, 4474, 4473, 4132, 4131, 4130, 4129, 4128, 4127, 4126, 4125, 4124, 4123, 118, 415, 433, 434, 436, 437, 439, 1528, 2495, 2496, 2715, 2953, 3438, 3862, 4308, 4398, 4399, 4424, 4662, 4762, 4810, 4883, 4884, 5134, 5859, 6098, 209, 1964, 4771, 4772, 4773, 4774, 4776, 5558, 5559, 5560, 5614, 5667, 5709, 5858, 2548, 182, 2599, 3867, 5862, 5876, 5995, 446, 441, 381, 4288, 4287, 4274, 4273, 3916, 3915, 381, 3764, 3603, 3264, 2006, 1512, 5416, 5417, 5418, 5419, 5851, 227, 355, 3765, 355, 221, 227, 5415, 441, 4493, 4288, 4287, 4274, 4273, 3916, 3915, 3825, 3765, 3764, 3603, 3264, 2645, 2202, 2006, 1512, 405, 6098, 5995, 5876, 5862, 5860, 5859, 5858, 5709, 5667, 5557, 5551, 5550, 5549, 5548, 3621, 1879, 1878, 1877, 1876, 1875, 1874, 1009, 1003, 754, 753, 752, 751, 749, 748, 747, 746, 745, 744, 743, 742, 741, 740, 739, 738, 737, 736, 735, 734, 733, 403, 398, 6348, 3694, 3113, 2744, 2743, 183, 262, 685, 687, 759, 760, 761, 762, 763, 764, 765, 766, 767, 770, 771, 2606, 2607, 2608, 2742, 2609, 2610, 2611, 2612, 2613, 2614, 2627, 2628, 2718, 2740, 2741, 4771, 175, 178, 181, 182, 209, 1964, 2356, 2548, 2596, 2599, 3327, 3867, 4772, 4773, 4774, 4776, 5558, 5559, 5560, 5614, 5667, 5709, 5858, 5859, 5862, 5876, 5995, 6098, 6207, 2199, 2200, 2201, 2202, 2203, 2593, 2920, 2921, 3405, 3406, 4727, 4728, 4757, 4758, 5754, 5773, 2204, 2205, 2206, 254, 333, 499, 2198, 4805, 5265, 5266, 6109, 6110, 6144, 6145, 6146, 6147, 6148, 6149, 6150, 6206, 6346, 2691, 2692, 2760, 2761, 2762, 2763, 2764, 2765, 2766, 2767, 2769, 2919, 2920, 2921, 3113, 3169, 3171, 3172, 3343, 3344, 3345, 3442, 3443, 3444, 3445, 3632, 3652, 3653, 3654, 3655, 3656, 3657, 3658, 3659, 3661, 1705, 1880, 1881, 262, 685, 687, 688, 689, 690, 691, 1882, 2185, 2186, 2187, 2188, 2189, 2190, 2191, 2202, 692, 129, 131, 145, 212, 2203, 226, 684, 565, 771, 1702, 1703, 2260, 2648, 665, 681, 682, 770, 683, 3662, 3663, 3664, 3665, 3666, 3694, 3732, 2690, 4559, 4600, 4804, 5196, 6098, 5995, 5876, 5862, 5860, 5859, 5858, 5709, 5667, 5197, 5134, 4884, 4883, 4878, 4810, 4762, 4662, 4424, 4416, 4399, 4398, 4377, 4376, 4308, 3863, 3862, 3438, 2953, 2930, 2715, 2496, 2495, 1532, 1531, 1530, 1529, 1528, 1133, 850, 439, 438, 437, 436, 435, 434, 433, 432, 415, 387, 180, 4127, 4128, 4129, 4130, 4131, 4132, 4473, 4474, 4475, 4476, 4477, 4478, 4479, 4480, 4481, 4491, 4599, 4790, 4791, 118, 4123, 4124, 4125, 4126, 5393, 4125, 4126, 4127, 4128, 4129, 4130, 4131, 4132, 4473, 4474, 4475, 4476, 4477, 4478, 4479, 4480, 4481, 4491, 4599, 4790, 4791, 4123, 118, 6217, 5501, 5394, 4124, 5315, 287, 456, 457, 458, 459, 460, 461, 462, 1031, 1037, 1038, 1039, 2454, 2721, 2739, 3149, 3347, 3940, 5263, 1964, 1887, 525, 5687, 276, 415, 483, 1107, 2159, 2703, 3480, 4085, 4376, 4424, 4547, 4662, 4878, 4884, 4960, 4961, 5026, 5454, 5455, 5579, 5592, 5593, 5594, 5595, 5596, 5597, 5601, 5602, 5604, 5632, 5667, 5668, 5669, 5679, 5680, 5681, 5682, 5683, 5684, 5685, 5686, 5688, 5689, 5690, 5691, 5692, 5693, 5694, 5695, 5696, 5697, 5698, 5699, 5700, 5701, 5702, 5703, 5704, 5705, 5706, 5707, 5708, 5709, 5710, 5711, 5858, 5859, 5860, 5862, 5876, 5995, 6098, 6405, 282, 503, 504, 507, 840, 842, 1141, 2400, 2740, 2831, 3330, 3940, 6093, 6091, 5783, 5782, 5781, 5394, 5101, 5862, 5876, 5995, 6098, 407, 5484, 5485, 5486, 5487, 5488, 5489, 5490, 5491, 5492, 5493, 5494, 5495, 5614, 5667, 5709, 5858, 5859, 5860, 4297, 4237, 4236, 4235, 4232, 4231, 4230, 3867, 3514, 3513, 3510, 2848, 1914, 1885, 531, 424, 423, 414, 398, 412, 5483, 5482, 5481, 4878, 4552, 4447, 4446, 5589, 5604, 5605, 5624, 5667, 5709, 5858, 5859, 5860, 5862, 5876, 5995, 6098, 2173, 837, 751, 435, 5587, 5586, 3762, 4344, 439, 728, 3189, 4338, 4339, 4340, 4341, 4342, 4343, 4878, 5556, 6223, 4790, 4791, 4131, 4130, 4129, 6223, 6098, 4128, 4127, 4126, 4125, 4124, 4123, 118, 131, 191, 197, 201, 728, 1749, 1749, 3228, 3340, 3621, 3653, 3653, 131, 3658, 3658, 3663, 3663, 4398, 4750, 4802, 4878, 4883, 4884, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 5026, 5027, 5028, 5088, 5614, 5613, 5612, 5611, 5610, 5609, 5608, 5607, 5606, 5227, 5570, 5538, 5228, 5995, 5876, 5862, 5860, 5858, 5709, 5667, 4132, 4473, 4474, 4475, 4476, 4477, 4478, 4479, 4480, 4481, 4491, 4599]

l2 = [255, 256, 257, 258, 259, 260, 261, 262, 264, 265, 337, 444, 446, 574, 731, 1002, 1004, 1008, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1852, 1995, 2005, 2521, 2609, 2920, 2921, 3470, 3471, 4692, 6388, 6389, 6390, 6412, 6413, 6414, 6415, 73, 118, 129, 131, 158, 267, 268, 269, 270, 271, 272, 440, 824, 847, 945, 1003, 1009, 1739, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 2462, 2701, 2739, 2920, 2921, 3278, 3365, 3366, 3367, 3368, 3369, 3370, 3371, 3463, 3602, 3603, 3638, 3639, 3640, 3641, 3642, 3643, 3644, 3645, 3650, 3652, 3653, 3654, 3655, 3656, 3658, 3659, 3661, 3662, 3663, 3664, 3665, 3666, 4018, 4264, 4311, 4378, 4379, 4448, 4782, 5026, 5027, 5028, 5088, 5603, 118, 251, 252, 642, 1768, 1770, 3523, 3979, 3987, 3989, 4015, 4670, 5026, 5443, 5727, 5838, 6125, 6362, 6397, 118, 399, 1002, 1907, 2162, 2207, 2208, 2209, 2210, 2211, 2258, 3222, 4187, 4188, 4189, 4190, 4191, 4192, 4400, 4401, 4402, 4403, 4471, 5617, 5618, 5793, 5794, 5800, 6100, 6101, 592, 593, 596, 597, 598, 282, 291, 462, 562, 565, 567, 784, 840, 946, 948, 949, 951, 953, 955, 959, 1040, 1399, 2425, 2631, 2636, 2663, 2831, 3149, 3150, 3156, 3719, 3720, 3733, 3790, 3935, 3936, 3940, 4084, 4145, 4146, 4147, 4148, 4149, 4150, 4151, 4152, 4153, 4154, 4155, 4156, 4157, 4158, 4159, 4161, 4162, 4266, 4278, 4280, 4281, 4282, 4283, 4499, 4500, 4501, 4706, 4806, 4901, 5009, 5010, 5011, 5012, 5026, 5087, 5309, 5779, 5811, 6121, 6122, 6162, 6253, 6254, 6255, 6366, 6367, 6368, 4455, 5211, 5212, 5213, 5214, 5279, 5280, 6410, 245, 256, 262, 291, 333, 337, 840, 842, 1040, 2557, 2663, 2920, 3149, 3150, 4380, 4381, 4382, 4383, 4384, 4385, 4455, 4456, 4457, 4458, 4459, 4460, 4461, 4462, 4499, 4500, 4501, 4966, 4967, 6349, 399, 2208, 2211, 2224, 2226, 4190, 4191, 4471, 4547, 4548, 4549, 4550, 4551, 4665, 5667, 5709, 5858, 5859, 5860, 5862, 5876, 5995, 6098, 6291, 118, 4123, 4124, 4125, 4126, 4127, 4128, 4129, 4130, 4131, 4132, 4473, 4474, 4475, 4476, 4477, 4478, 4479, 4480, 4481, 4491, 4599, 4790, 4791, 605, 609, 2660, 5779, 6366, 6367, 6368, 6371, 6373, 6374, 605, 609, 2660, 5779, 6366, 6367, 6368, 6371, 6373, 6374, 501, 635, 5443, 5619, 5620, 5621, 5622, 5623, 5628, 6357]

am_ugdata = np.array([[255, 'Caitlin Winkworth', 24, 'Beiersdorf'],
       [256, 'Suzanne Irving', 24, 'Beiersdorf'],
       [257, 'Shannon Ahearn', 24, 'Beiersdorf'],
       [258, 'Peggy Costella', 24, 'Beiersdorf'],
       [259, 'Mikayla Mason', 24, 'Beiersdorf'],
       [260, 'Cristina Criado', 24, 'Beiersdorf'],
       [261, 'Marissa Roney', 24, 'Beiersdorf'],
       [262, 'Brooke Lipschitz', 24, 'Beiersdorf'],
       [264, 'Matthew Herschlein', 24, 'Beiersdorf'],
       [265, 'Julia Giaimo', 24, 'Beiersdorf'],
       [337, 'Mary Dailey', 24, 'Beiersdorf'],
       [444, 'morgan leathers', 24, 'Beiersdorf'],
       [446, 'abbey sherrard', 24, 'Beiersdorf'],
       [574, 'Cali Mills', 24, 'Beiersdorf'],
       [731, 'Erin Stenwall', 24, 'Beiersdorf'],
       [1002, 'Kaitlin Debacker', 24, 'Beiersdorf'],
       [1004, 'Lisa Evans', 24, 'Beiersdorf'],
       [1008, 'Aaron Edington', 24, 'Beiersdorf'],
       [1818, 'Jeremy Rosenblum', 24, 'Beiersdorf'],
       [1819, 'Vincent LaBarbara', 24, 'Beiersdorf'],
       [1820, 'Ryan Love', 24, 'Beiersdorf'],
       [1821, 'Isabel Javit', 24, 'Beiersdorf'],
       [1822, 'Tracey Wexler', 24, 'Beiersdorf'],
       [1823, 'Fabio Goncalves', 24, 'Beiersdorf'],
       [1824, 'Carson Pope', 24, 'Beiersdorf'],
       [1825, 'Jonathan Dennis', 24, 'Beiersdorf'],
       [1826, 'Tom Kirwan', 24, 'Beiersdorf'],
       [1827, 'Tamara Strelnykova', 24, 'Beiersdorf'],
       [1828, 'Rebecca Stanley', 24, 'Beiersdorf'],
       [1852, 'Mara Behar', 24, 'Beiersdorf'],
       [1995, 'Lori Chapman', 24, 'Beiersdorf'],
       [2005, 'Anthony McCarthy', 24, 'Beiersdorf'],
       [2521, 'Margaret Tibbitts', 24, 'Beiersdorf'],
       [2609, 'owen waters', 24, 'Beiersdorf'],
       [2920, 'Georgina Thomson', 24, 'Beiersdorf'],
       [2921, 'Charles Cebuhar', 24, 'Beiersdorf'],
       [3470, 'Alexis Dudas', 24, 'Beiersdorf'],
       [3471, 'Catherine Meixner', 24, 'Beiersdorf'],
       [4692, 'Karen Larson', 24, 'Beiersdorf'],
       [6388, 'Michael Hackett', 24, 'Beiersdorf'],
       [6389, 'Jessica Lucrezia', 24, 'Beiersdorf'],
       [6390, 'Sara Abdeinaby', 24, 'Beiersdorf'],
       [6412, 'Ivy Lin', 24, 'Beiersdorf'],
       [6413, 'Katherine Maglione', 24, 'Beiersdorf'],
       [6414, 'Matt Schmerzler', 24, 'Beiersdorf'],
       [6415, 'Lauren Zukoff', 24, 'Beiersdorf'],
       [73, 'Sharon Cullen', 25, 'State Farm'],
       [118, 'Harrison Solomon', 25, 'State Farm'],
       [129, 'Matt Artingstall', 25, 'State Farm'],
       [131, 'Vamsi Patchamatla', 25, 'State Farm'],
       [158, 'Katie Forrer', 25, 'State Farm'],
       [267, 'Elliott Woodruff', 25, 'State Farm'],
       [268, 'Alexander Payne', 25, 'State Farm'],
       [269, 'Edward Schmitt', 25, 'State Farm'],
       [270, 'Caroline Navarro', 25, 'State Farm'],
       [271, 'Sean Sattel', 25, 'State Farm'],
       [272, 'Alex Vossen', 25, 'State Farm'],
       [440, 'Doug Hall', 25, 'State Farm'],
       [824, 'Madi Krizan', 25, 'State Farm'],
       [847, 'Zane AnnalectTest', 25, 'State Farm'],
       [945, 'Deirdre McNally', 25, 'State Farm'],
       [1003, 'Kristen Koepsel', 25, 'State Farm'],
       [1009, 'Erin Neal', 25, 'State Farm'],
       [1739, 'Marissa Stampolis', 25, 'State Farm'],
       [1893, 'katherine schaffer', 25, 'State Farm'],
       [1894, 'Stephanie Angelo', 25, 'State Farm'],
       [1895, 'Madison Glaeser', 25, 'State Farm'],
       [1896, 'Matthew Maxon', 25, 'State Farm'],
       [1897, 'Nate Bianchi', 25, 'State Farm'],
       [1898, 'Brenda Teruel', 25, 'State Farm'],
       [1899, 'Brenda Chan', 25, 'State Farm'],
       [1900, 'Kaihtlyn Schlachter', 25, 'State Farm'],
       [2462, 'jamie murphy', 25, 'State Farm'],
       [2701, 'Rahul Gaadhe', 25, 'State Farm'],
       [2739, 'Alex Siddall', 25, 'State Farm'],
       [2920, 'Georgina Thomson', 25, 'State Farm'],
       [2921, 'Charles Cebuhar', 25, 'State Farm'],
       [3278, 'Tim Young', 25, 'State Farm'],
       [3365, 'Craig Sherwood', 25, 'State Farm'],
       [3366, 'Umeshwari Nadkarni', 25, 'State Farm'],
       [3367, 'Jack Meyer', 25, 'State Farm'],
       [3368, 'Daniel Gallagher', 25, 'State Farm'],
       [3369, 'John Ninivaggi', 25, 'State Farm'],
       [3370, 'Mark Kieblesz', 25, 'State Farm'],
       [3371, 'Shari Staiano', 25, 'State Farm'],
       [3463, 'dave kornett', 25, 'State Farm'],
       [3602, 'Deidra Oboyle', 25, 'State Farm'],
       [3603, 'Autumn Watts', 25, 'State Farm'],
       [3638, 'hannah tunstall', 25, 'State Farm'],
       [3639, 'josh todd', 25, 'State Farm'],
       [3640, 'louisa vazquez', 25, 'State Farm'],
       [3641, 'joshua sherden', 25, 'State Farm'],
       [3642, 'jay heininger', 25, 'State Farm'],
       [3643, 'shannon healy', 25, 'State Farm'],
       [3644, 'gabe heller', 25, 'State Farm'],
       [3645, 'ashley bain', 25, 'State Farm'],
       [3650, 'alvin leung', 25, 'State Farm'],
       [3652, 'aishwarya sharma', 25, 'State Farm'],
       [3653, 'tabitha Anderson', 25, 'State Farm'],
       [3654, 'john ericson', 25, 'State Farm'],
       [3655, 'nathan brown', 25, 'State Farm'],
       [3656, 'valerie nguyen', 25, 'State Farm'],
       [3658, 'ashwini paunikar', 25, 'State Farm'],
       [3659, 'robyn oreilly', 25, 'State Farm'],
       [3661, 'Andrew Gewercman', 25, 'State Farm'],
       [3662, 'Gloria Roncancio', 25, 'State Farm'],
       [3663, 'Indranil Datta', 25, 'State Farm'],
       [3664, 'trudi miller', 25, 'State Farm'],
       [3665, 'Sarah Druett', 25, 'State Farm'],
       [3666, 'sarah darilmaz', 25, 'State Farm'],
       [4018, 'parvathi mukundan', 25, 'State Farm'],
       [4264, 'connor schweisberger', 25, 'State Farm'],
       [4311, 'Bryan Krebs', 25, 'State Farm'],
       [4378, 'James Kanak', 25, 'State Farm'],
       [4379, 'Matt Oster', 25, 'State Farm'],
       [4448, 'windia dieudonne', 25, 'State Farm'],
       [4782, 'Ben Dreyfuss', 25, 'State Farm'],
       [5026, 'Sean Pinkney', 25, 'State Farm'],
       [5027, 'Jennifer Villany', 25, 'State Farm'],
       [5028, 'Marc Rossen', 25, 'State Farm'],
       [5088, 'Jamie Khoo', 25, 'State Farm'],
       [5603, 'Kalika Saxena', 25, 'State Farm'],
       [118, 'Harrison Solomon', 46, 'Wells Fargo'],
       [251, 'Maegan Butler', 46, 'Wells Fargo'],
       [252, 'Eileen McGillicuddy', 46, 'Wells Fargo'],
       [642, 'Paige Glassman', 46, 'Wells Fargo'],
       [1768, 'David Moreno', 46, 'Wells Fargo'],
       [1770, 'Nicholas Sena', 46, 'Wells Fargo'],
       [3523, 'Lizzy Pedigo', 46, 'Wells Fargo'],
       [3979, 'Victoria Brigham', 46, 'Wells Fargo'],
       [3987, 'Melissa Simonelli', 46, 'Wells Fargo'],
       [3989, 'Gavin Shelton', 46, 'Wells Fargo'],
       [4015, 'Sandra Flores', 46, 'Wells Fargo'],
       [4670, 'Jennifer  Porile', 46, 'Wells Fargo'],
       [5026, 'Sean Pinkney', 46, 'Wells Fargo'],
       [5443, 'Kiran Sridhar', 46, 'Wells Fargo'],
       [5727, 'Catherine  Test for ENG-44675', 46, 'Wells Fargo'],
       [5838, 'Anna Lockward', 46, 'Wells Fargo'],
       [6125, 'Danica Duenas', 46, 'Wells Fargo'],
       [6362, 'Elizabeth Ortiz', 46, 'Wells Fargo'],
       [6397, 'Josue Martinez', 46, 'Wells Fargo'],
       [118, 'Harrison Solomon', 1083, 'Mercedes Benz'],
       [399, 'Renee Tozzi', 1083, 'Mercedes Benz'],
       [1002, 'Kaitlin Debacker', 1083, 'Mercedes Benz'],
       [1907, 'Monica Wiedemann', 1083, 'Mercedes Benz'],
       [2162, 'Rachel Dankner', 1083, 'Mercedes Benz'],
       [2207, 'Melissa Whitcomb', 1083, 'Mercedes Benz'],
       [2208, 'Hallie Bates', 1083, 'Mercedes Benz'],
       [2209, 'Allison Bobruska', 1083, 'Mercedes Benz'],
       [2210, 'sarah prince', 1083, 'Mercedes Benz'],
       [2211, 'tommy orme', 1083, 'Mercedes Benz'],
       [2258, 'Adam Arnegger', 1083, 'Mercedes Benz'],
       [3222, 'ahmad nashef', 1083, 'Mercedes Benz'],
       [4187, 'Hailey McInnes', 1083, 'Mercedes Benz'],
       [4188, 'Bailey Battle', 1083, 'Mercedes Benz'],
       [4189, 'Amelia bermingham', 1083, 'Mercedes Benz'],
       [4190, 'Alyssa Pachter', 1083, 'Mercedes Benz'],
       [4191, 'arantxa capellan', 1083, 'Mercedes Benz'],
       [4192, 'soojin yun', 1083, 'Mercedes Benz'],
       [4400, 'Amy Becker', 1083, 'Mercedes Benz'],
       [4401, 'Hope Henry', 1083, 'Mercedes Benz'],
       [4402, 'Emma Jensen', 1083, 'Mercedes Benz'],
       [4403, 'Riley Patterson', 1083, 'Mercedes Benz'],
       [4471, 'Kim Heller', 1083, 'Mercedes Benz'],
       [5617, 'Lana Darwan', 1083, 'Mercedes Benz'],
       [5618, 'Olivia Dal Porto', 1083, 'Mercedes Benz'],
       [5793, 'matthew habersaat', 1083, 'Mercedes Benz'],
       [5794, 'Lindsey Lomuto', 1083, 'Mercedes Benz'],
       [5800, 'Rudy Gainey', 1083, 'Mercedes Benz'],
       [6100, 'Phoebe Casey', 1083, 'Mercedes Benz'],
       [6101, 'Matthew Kupfer', 1083, 'Mercedes Benz'],
       [592, 'Christopher Stanger', 170, 'AT&T - ABS'],
       [593, 'Lisa Danon', 170, 'AT&T - ABS'],
       [596, 'Jordan Bundy', 170, 'AT&T - ABS'],
       [597, 'Nadalie Balmer', 170, 'AT&T - ABS'],
       [598, 'Michael Noah', 170, 'AT&T - ABS'],
       [566, 'Catherine McNamara', 43, 'AT&T Consumer'],
       [567, 'Michael Napoli', 43, 'AT&T Consumer'],
       [568, 'Joseph Sebolao', 43, 'AT&T Consumer'],
       [569, 'Nathan Kasmanoff', 43, 'AT&T Consumer'],
       [570, 'Amanda Clemens', 43, 'AT&T Consumer'],
       [572, 'Kyle Knutsen', 43, 'AT&T Consumer'],
       [574, 'Cali Mills', 43, 'AT&T Consumer'],
       [575, 'Alexa Kennedy', 43, 'AT&T Consumer'],
       [576, 'William Kuzel', 43, 'AT&T Consumer'],
       [592, 'Christopher Stanger', 43, 'AT&T Consumer'],
       [593, 'Lisa Danon', 43, 'AT&T Consumer'],
       [594, 'Chris Beesley', 43, 'AT&T Consumer'],
       [595, 'Madeline Langdon', 43, 'AT&T Consumer'],
       [596, 'Jordan Bundy', 43, 'AT&T Consumer'],
       [597, 'Nadalie Balmer', 43, 'AT&T Consumer'],
       [598, 'Michael Noah', 43, 'AT&T Consumer'],
       [602, 'Christiana Messina', 43, 'AT&T Consumer'],
       [603, 'Tavo Castro', 43, 'AT&T Consumer'],
       [604, 'Chantal Villain', 43, 'AT&T Consumer'],
       [605, 'Adam Block', 43, 'AT&T Consumer'],
       [607, 'Travis Miller', 43, 'AT&T Consumer'],
       [608, 'Mai Hoang', 43, 'AT&T Consumer'],
       [609, 'Jeff Fisher', 43, 'AT&T Consumer'],
       [610, 'Leticia Juarez', 43, 'AT&T Consumer'],
       [784, 'Alyson Civitano', 43, 'AT&T Consumer'],
       [881, 'Jing Suk', 43, 'AT&T Consumer'],
       [948, 'Julianna Bowman', 43, 'AT&T Consumer'],
       [949, 'Neil Sorrentino', 43, 'AT&T Consumer'],
       [950, 'Stephen Basile', 43, 'AT&T Consumer'],
       [951, 'Mike Wolfensperger', 43, 'AT&T Consumer'],
       [966, 'Kim Simun-Janson', 43, 'AT&T Consumer'],
       [997, 'Nadalie Dias', 43, 'AT&T Consumer'],
       [998, 'Clara Cullen', 43, 'AT&T Consumer'],
       [1001, 'Jacqueline Goode', 43, 'AT&T Consumer'],
       [1005, 'Liz Pelikan', 43, 'AT&T Consumer'],
       [1033, 'Samantha  Wilson', 43, 'AT&T Consumer'],
       [1040, 'Bryan Vargas', 43, 'AT&T Consumer'],
       [1238, 'Ryan Grogan', 43, 'AT&T Consumer'],
       [1307, 'Jordan Brodbeck', 43, 'AT&T Consumer'],
       [1361, 'April Coen', 43, 'AT&T Consumer'],
       [2069, 'Moriah Mclaughlin', 43, 'AT&T Consumer'],
       [2259, 'david doerner', 43, 'AT&T Consumer'],
       [2281, 'alison choi', 43, 'AT&T Consumer'],
       [2512, 'Jasmin Davis', 43, 'AT&T Consumer'],
       [2629, 'Geoffrey Spies', 43, 'AT&T Consumer'],
       [2630, 'robert rizzo', 43, 'AT&T Consumer'],
       [2631, 'melissa mcdevitt', 43, 'AT&T Consumer'],
       [2632, 'Chris Cotter', 43, 'AT&T Consumer'],
       [2633, 'Greg Lawrence', 43, 'AT&T Consumer'],
       [2634, 'paige king', 43, 'AT&T Consumer'],
       [2635, 'caroline taylor', 43, 'AT&T Consumer'],
       [2636, 'Scott Irace', 43, 'AT&T Consumer'],
       [2637, 'cara tringali', 43, 'AT&T Consumer'],
       [2659, 'alex ornstein', 43, 'AT&T Consumer'],
       [2660, 'Allan silver', 43, 'AT&T Consumer'],
       [2662, 'Andres torrente', 43, 'AT&T Consumer'],
       [2663, 'brian diamond', 43, 'AT&T Consumer'],
       [2664, 'brook hauge', 43, 'AT&T Consumer'],
       [2665, 'caelin beesemyer', 43, 'AT&T Consumer'],
       [2666, 'James Aquila', 43, 'AT&T Consumer'],
       [2667, 'janice chung', 43, 'AT&T Consumer'],
       [2669, 'katie mcgregor', 43, 'AT&T Consumer'],
       [2670, 'Krystyne silos', 43, 'AT&T Consumer'],
       [2671, 'Matt decuir', 43, 'AT&T Consumer'],
       [2672, 'nathan valencia', 43, 'AT&T Consumer'],
       [2673, 'richard vietri', 43, 'AT&T Consumer'],
       [2674, 'yoona bae', 43, 'AT&T Consumer'],
       [2676, 'Test Permissioning User AT&T', 43, 'AT&T Consumer'],
       [2677, 'Dylan Fowler', 43, 'AT&T Consumer'],
       [2678, 'Max Germain', 43, 'AT&T Consumer'],
       [2679, 'brian wesche', 43, 'AT&T Consumer'],
       [2680, 'atche.portillo@hearts-science.com portillo', 43,'AT&T Consumer'],
       [2810, 'Gabriella Carrafiello', 43, 'AT&T Consumer'],
       [2836, 'Chelcie Demarco', 43, 'AT&T Consumer'],
       [2843, 'Jordan Trevino', 43, 'AT&T Consumer'],
       [5011, 'Leeanne Larue', 43, 'AT&T Consumer'],
       [5012, 'Omar Belkhiter', 43, 'AT&T Consumer'],
       [4499, 'Kaitlyn McInnis', 43, 'AT&T Consumer'],
       [4418, 'cole demert', 43, 'AT&T Consumer'],
       [4283, 'Sabrina Schnapp', 43, 'AT&T Consumer'],
       [4282, 'Maggy Powers', 43, 'AT&T Consumer'],
       [4281, 'Rachel Flynn', 43, 'AT&T Consumer'],
       [4280, 'Brittany Gelman', 43, 'AT&T Consumer'],
       [4278, 'Matthew Romansky', 43, 'AT&T Consumer'],
       [4277, 'Nicholas Youngman', 43, 'AT&T Consumer'],
       [4158, 'natasha gold', 43, 'AT&T Consumer'],
       [4153, 'neil messing', 43, 'AT&T Consumer'],
       [3940, 'JoAnn Sciarrino', 43, 'AT&T Consumer'],
       [3936, 'Stephanie  Morris', 43, 'AT&T Consumer'],
       [3935, 'Kelly Young', 43, 'AT&T Consumer'],
       [3790, 'sana jawaid', 43, 'AT&T Consumer'],
       [3733, 'Rebecca Yi', 43, 'AT&T Consumer'],
       [3720, 'abraham madampil', 43, 'AT&T Consumer'],
       [3719, 'alba cuevas', 43, 'AT&T Consumer'],
       [3156, 'Jane  Reddan', 43, 'AT&T Consumer'],
       [3150, 'maryanne geiger', 43, 'AT&T Consumer'],
       [3149, 'maria depanfilis', 43, 'AT&T Consumer'],
       [5087, 'Hannah Wagner', 43, 'AT&T Consumer'],
       [5309, 'Alexander Hin', 43, 'AT&T Consumer'],
       [5779, 'Alan Lazebnik', 43, 'AT&T Consumer'],
       [5811, 'Bob Hunt', 43, 'AT&T Consumer'],
       [4500, 'Pam Amir', 43, 'AT&T Consumer'],
       [6349, 'Kerrie Piccolo', 43, 'AT&T Consumer'],
       [6366, 'Matt  Fomby', 43, 'AT&T Consumer'],
       [6367, 'Chase Crawford', 43, 'AT&T Consumer'],
       [6368, 'Amanda  Rager', 43, 'AT&T Consumer'],
       [4501, 'matt reed', 43, 'AT&T Consumer'],
       [4706, 'Caroline Murray', 43, 'AT&T Consumer'],
       [4806, 'kianna zielinski', 43, 'AT&T Consumer'],
       [4901, 'Jonathan Smith', 43, 'AT&T Consumer'],
       [5009, 'Neziah Goodman', 43, 'AT&T Consumer'],
       [5010, 'Ethan Kahn', 43, 'AT&T Consumer'],
       [118, 'Harrison Solomon', 43, 'AT&T Consumer'],
       [78, 'Jon Kaiser', 43, 'AT&T Consumer'],
       [282, 'Peejay Schmitt', 43, 'AT&T Consumer'],
       [562, 'Alexandra Braun', 43, 'AT&T Consumer'],
       [563, 'Casandra Levy', 43, 'AT&T Consumer'],
       [564, 'Eric Lyons', 43, 'AT&T Consumer'],
       [282, 'Peejay Schmitt', 2088, 'AT&T Cricket Wireless'],
       [291, 'Scott Minor', 2088, 'AT&T Cricket Wireless'],
       [462, 'Allison Preate', 2088, 'AT&T Cricket Wireless'],
       [562, 'Alexandra Braun', 2088, 'AT&T Cricket Wireless'],
       [565, 'Nick Pescuma', 2088, 'AT&T Cricket Wireless'],
       [567, 'Michael Napoli', 2088, 'AT&T Cricket Wireless'],
       [784, 'Alyson Civitano', 2088, 'AT&T Cricket Wireless'],
       [840, 'Frank Strehl', 2088, 'AT&T Cricket Wireless'],
       [946, 'Andrea Powers', 2088, 'AT&T Cricket Wireless'],
       [948, 'Julianna Bowman', 2088, 'AT&T Cricket Wireless'],
       [949, 'Neil Sorrentino', 2088, 'AT&T Cricket Wireless'],
       [951, 'Mike Wolfensperger', 2088, 'AT&T Cricket Wireless'],
       [953, 'Linnea Corn', 2088, 'AT&T Cricket Wireless'],
       [955, 'Kimberley Friedman', 2088, 'AT&T Cricket Wireless'],
       [959, 'Carter Ehlers', 2088, 'AT&T Cricket Wireless'],
       [1040, 'Bryan Vargas', 2088, 'AT&T Cricket Wireless'],
       [1399, 'Paul  Fitzgerald', 2088, 'AT&T Cricket Wireless'],
       [2425, 'Paul Robaszewski', 2088, 'AT&T Cricket Wireless'],
       [2631, 'melissa mcdevitt', 2088, 'AT&T Cricket Wireless'],
       [2636, 'Scott Irace', 2088, 'AT&T Cricket Wireless'],
       [2663, 'brian diamond', 2088, 'AT&T Cricket Wireless'],
       [2831, 'Courtney Overacker', 2088, 'AT&T Cricket Wireless'],
       [3149, 'maria depanfilis', 2088, 'AT&T Cricket Wireless'],
       [3150, 'maryanne geiger', 2088, 'AT&T Cricket Wireless'],
       [3156, 'Jane  Reddan', 2088, 'AT&T Cricket Wireless'],
       [3719, 'alba cuevas', 2088, 'AT&T Cricket Wireless'],
       [3720, 'abraham madampil', 2088, 'AT&T Cricket Wireless'],
       [3733, 'Rebecca Yi', 2088, 'AT&T Cricket Wireless'],
       [3790, 'sana jawaid', 2088, 'AT&T Cricket Wireless'],
       [3935, 'Kelly Young', 2088, 'AT&T Cricket Wireless'],
       [3936, 'Stephanie  Morris', 2088, 'AT&T Cricket Wireless'],
       [3940, 'JoAnn Sciarrino', 2088, 'AT&T Cricket Wireless'],
       [4084, 'Abigail  Rivera', 2088, 'AT&T Cricket Wireless'],
       [4145, 'daniel clark1', 2088, 'AT&T Cricket Wireless'],
       [4146, 'alison strain', 2088, 'AT&T Cricket Wireless'],
       [4147, 'Deanna cataldi', 2088, 'AT&T Cricket Wireless'],
       [4148, 'jacqueline golden', 2088, 'AT&T Cricket Wireless'],
       [4149, 'marit ripley', 2088, 'AT&T Cricket Wireless'],
       [4150, 'melissa richey', 2088, 'AT&T Cricket Wireless'],
       [4151, 'samantha ickovic', 2088, 'AT&T Cricket Wireless'],
       [4152, 'Eugene Kang', 2088, 'AT&T Cricket Wireless'],
       [4153, 'neil messing', 2088, 'AT&T Cricket Wireless'],
       [4154, 'Alisia frost', 2088, 'AT&T Cricket Wireless'],
       [4155, 'danielle rutherford', 2088, 'AT&T Cricket Wireless'],
       [4156, 'margo adams', 2088, 'AT&T Cricket Wireless'],
       [4157, 'mj giraldo', 2088, 'AT&T Cricket Wireless'],
       [4158, 'natasha gold', 2088, 'AT&T Cricket Wireless'],
       [4159, 'patricio cantuvaldes', 2088, 'AT&T Cricket Wireless'],
       [4161, 'sarah katsikas', 2088, 'AT&T Cricket Wireless'],
       [4162, 'Erika fleming', 2088, 'AT&T Cricket Wireless'],
       [4266, 'Deborah Kenney', 2088, 'AT&T Cricket Wireless'],
       [4278, 'Matthew Romansky', 2088, 'AT&T Cricket Wireless'],
       [4280, 'Brittany Gelman', 2088, 'AT&T Cricket Wireless'],
       [4281, 'Rachel Flynn', 2088, 'AT&T Cricket Wireless'],
       [4282, 'Maggy Powers', 2088, 'AT&T Cricket Wireless'],
       [4283, 'Sabrina Schnapp', 2088, 'AT&T Cricket Wireless'],
       [4499, 'Kaitlyn McInnis', 2088, 'AT&T Cricket Wireless'],
       [4500, 'Pam Amir', 2088, 'AT&T Cricket Wireless'],
       [4501, 'matt reed', 2088, 'AT&T Cricket Wireless'],
       [4706, 'Caroline Murray', 2088, 'AT&T Cricket Wireless'],
       [4806, 'kianna zielinski', 2088, 'AT&T Cricket Wireless'],
       [4901, 'Jonathan Smith', 2088, 'AT&T Cricket Wireless'],
       [5009, 'Neziah Goodman', 2088, 'AT&T Cricket Wireless'],
       [5010, 'Ethan Kahn', 2088, 'AT&T Cricket Wireless'],
       [5011, 'Leeanne Larue', 2088, 'AT&T Cricket Wireless'],
       [5012, 'Omar Belkhiter', 2088, 'AT&T Cricket Wireless'],
       [5026, 'Sean Pinkney', 2088, 'AT&T Cricket Wireless'],
       [5087, 'Hannah Wagner', 2088, 'AT&T Cricket Wireless'],
       [5309, 'Alexander Hin', 2088, 'AT&T Cricket Wireless'],
       [5779, 'Alan Lazebnik', 2088, 'AT&T Cricket Wireless'],
       [5811, 'Bob Hunt', 2088, 'AT&T Cricket Wireless'],
       [6121, 'Xinwen Zhang', 2088, 'AT&T Cricket Wireless'],
       [6122, 'Justin Smith', 2088, 'AT&T Cricket Wireless'],
       [6162, 'Anant Veeravalli', 2088, 'AT&T Cricket Wireless'],
       [6253, 'Erika  Wasonoredjo ', 2088, 'AT&T Cricket Wireless'],
       [6254, 'Moya  Leung', 2088, 'AT&T Cricket Wireless'],
       [6255, 'Sharmaine Francois', 2088, 'AT&T Cricket Wireless'],
       [6366, 'Matt  Fomby', 2088, 'AT&T Cricket Wireless'],
       [6367, 'Chase Crawford', 2088, 'AT&T Cricket Wireless'],
       [6368, 'Amanda  Rager', 2088, 'AT&T Cricket Wireless'],
       [4455, 'Jason Tennenbaum', 3102, 'DIRECTV'],
       [5211, 'Corinna  Wu', 3102, 'DIRECTV'],
       [5212, 'David  Johnson', 3102, 'DIRECTV'],
       [5213, 'Nancy Kuo', 3102, 'DIRECTV'],
       [5214, 'Shiloh Bae', 3102, 'DIRECTV'],
       [5279, 'Minghao Bian', 3102, 'DIRECTV'],
       [5280, 'Sai Yadalam', 3102, 'DIRECTV'],
       [6410, 'Kristen  Wong', 3102, 'DIRECTV'],
       [245, 'Melissa Klein', 3102, 'DIRECTV'],
       [256, 'Suzanne Irving', 3102, 'DIRECTV'],
       [262, 'Brooke Lipschitz', 3102, 'DIRECTV'],
       [291, 'Scott Minor', 3102, 'DIRECTV'],
       [333, 'Will Romann', 3102, 'DIRECTV'],
       [337, 'Mary Dailey', 3102, 'DIRECTV'],
       [840, 'Frank Strehl', 3102, 'DIRECTV'],
       [842, 'Natalie Polanger', 3102, 'DIRECTV'],
       [1040, 'Bryan Vargas', 3102, 'DIRECTV'],
       [2557, 'cindy chang', 3102, 'DIRECTV'],
       [2663, 'brian diamond', 3102, 'DIRECTV'],
       [2920, 'Georgina Thomson', 3102, 'DIRECTV'],
       [3149, 'maria depanfilis', 3102, 'DIRECTV'],
       [3150, 'maryanne geiger', 3102, 'DIRECTV'],
       [4380, 'colleen fox', 3102, 'DIRECTV'],
       [4381, 'serena boglino', 3102, 'DIRECTV'],
       [4382, 'Sam kornblau', 3102, 'DIRECTV'],
       [4383, 'Brent barker', 3102, 'DIRECTV'],
       [4384, 'Kevin an', 3102, 'DIRECTV'],
       [4385, 'Mark guzik', 3102, 'DIRECTV'],
       [4455, 'Jason Tennenbaum', 3102, 'DIRECTV'],
       [4456, 'George Wu', 3102, 'DIRECTV'],
       [4457, 'Mark Loovis', 3102, 'DIRECTV'],
       [4458, 'Dora Lorenzo', 3102, 'DIRECTV'],
       [4459, 'Roy Nehmeh', 3102, 'DIRECTV'],
       [4460, 'Faryn Hill', 3102, 'DIRECTV'],
       [4461, 'Lisa Bakewell', 3102, 'DIRECTV'],
       [4462, 'Joey Lafleur', 3102, 'DIRECTV'],
       [4499, 'Kaitlyn McInnis', 3102, 'DIRECTV'],
       [4500, 'Pam Amir', 3102, 'DIRECTV'],
       [4501, 'matt reed', 3102, 'DIRECTV'],
       [4966, 'Sajid Patel', 3102, 'DIRECTV'],
       [4967, 'Curt Kaneshiro', 3102, 'DIRECTV'],
       [6349, 'Kerrie Piccolo', 3102, 'DIRECTV'],
       [399, 'Renee Tozzi', 3169, 'Idorsia'],
       [2208, 'Hallie Bates', 3169, 'Idorsia'],
       [2211, 'tommy orme', 3169, 'Idorsia'],
       [2224, 'Nicole Walter', 3169, 'Idorsia'],
       [2226, 'Mindy Rosenthal', 3169, 'Idorsia'],
       [4190, 'Alyssa Pachter', 3169, 'Idorsia'],
       [4191, 'arantxa capellan', 3169, 'Idorsia'],
       [4471, 'Kim Heller', 3169, 'Idorsia'],
       [4547, 'Trevor  Buchmayr ', 3169, 'Idorsia'],
       [4548, 'Wesley Wall', 3169, 'Idorsia'],
       [4549, 'Nicole Walter', 3169, 'Idorsia'],
       [4550, 'Suzie  Woldeab', 3169, 'Idorsia'],
       [4551, 'Sophia Leitner', 3169, 'Idorsia'],
       [4665, 'Caitlin Falvey', 3169, 'Idorsia'],
       [5667, 'Susan Wallace', 3169, 'Idorsia'],
       [5709, 'Tiffany Mullan', 3169, 'Idorsia'],
       [5858, 'Amanda  Seepersaud', 3169, 'Idorsia'],
       [5859, 'Hannah Kelsen', 3169, 'Idorsia'],
       [5860, 'Leslie Hammons', 3169, 'Idorsia'],
       [5862, 'Sara  Luczynski', 3169, 'Idorsia'],
       [5876, 'Anastasia Derbas', 3169, 'Idorsia'],
       [5995, 'Christian Lezama', 3169, 'Idorsia'],
       [6098, 'Xavier Eaves', 3169, 'Idorsia'],
       [6291, 'Laura Goldin', 3169, 'Idorsia'],
       [118, 'Harrison Solomon', 3438, 'State Farm'],
       [4123, 'Beth Rockwood', 3438, 'State Farm'],
       [4124, 'Mariel Estrada', 3438, 'State Farm'],
       [4125, 'Kailyn Hartmann', 3438, 'State Farm'],
       [4126, 'John Yanni', 3438, 'State Farm'],
       [4127, 'Sharuk Ali', 3438, 'State Farm'],
       [4128, 'Jen DeVito', 3438, 'State Farm'],
       [4129, 'Michele Resnick', 3438, 'State Farm'],
       [4130, 'Rob Weissberg', 3438, 'State Farm'],
       [4131, 'Juan Gomez', 3438, 'State Farm'],
       [4132, 'Matt Gold', 3438, 'State Farm'],
       [4473, 'Noelle Huynh', 3438, 'State Farm'],
       [4474, 'Robert Bienes', 3438, 'State Farm'],
       [4475, 'Stephanie Posada', 3438, 'State Farm'],
       [4476, 'Katherine Mitrotasios', 3438, 'State Farm'],
       [4477, 'Tania Houston', 3438, 'State Farm'],
       [4478, 'Ana Popkowski', 3438, 'State Farm'],
       [4479, 'Amy Digregorio', 3438, 'State Farm'],
       [4480, 'Katherine Reyes Butkowski', 3438, 'State Farm'],
       [4481, 'Reshma Shah', 3438, 'State Farm'],
       [4491, 'Taylor Clarke', 3438, 'State Farm'],
       [4599, 'Stephanie Coto', 3438, 'State Farm'],
       [4790, 'Jennifer Yurko', 3438, 'State Farm'],
       [4791, 'Heather Coghill', 3438, 'State Farm'],
       [605, 'Adam Block', 3527, 'AT&T Local Internet'],
       [609, 'Jeff Fisher', 3527, 'AT&T Local Internet'],
       [2660, 'Allan silver', 3527, 'AT&T Local Internet'],
       [5779, 'Alan Lazebnik', 3527, 'AT&T Local Internet'],
       [6366, 'Matt  Fomby', 3527, 'AT&T Local Internet'],
       [6367, 'Chase Crawford', 3527, 'AT&T Local Internet'],
       [6368, 'Amanda  Rager', 3527, 'AT&T Local Internet'],
       [6371, 'Beth Boudart', 3527, 'AT&T Local Internet'],
       [6373, 'Sandra Ramos', 3527, 'AT&T Local Internet'],
       [6374, 'Gianna Martin-Duarte', 3527, 'AT&T Local Internet'],
       [605, 'Adam Block', 3527, 'AT&T Local Internet'],
       [609, 'Jeff Fisher', 3527, 'AT&T Local Internet'],
       [2660, 'Allan silver', 3527, 'AT&T Local Internet'],
       [5779, 'Alan Lazebnik', 3527, 'AT&T Local Internet'],
       [6366, 'Matt  Fomby', 3527, 'AT&T Local Internet'],
       [6367, 'Chase Crawford', 3527, 'AT&T Local Internet'],
       [6368, 'Amanda  Rager', 3527, 'AT&T Local Internet'],
       [6371, 'Beth Boudart', 3527, 'AT&T Local Internet'],
       [6373, 'Sandra Ramos', 3527, 'AT&T Local Internet'],
       [6374, 'Gianna Martin-Duarte', 3527, 'AT&T Local Internet'],
       [501, 'Sean Yang', 3713, 'Wells Fargo ENT'],
       [635, 'Francisca Resendez', 3713, 'Wells Fargo ENT'],
       [5443, 'Kiran Sridhar', 3713, 'Wells Fargo ENT'],
       [5619, 'Claire He', 3713, 'Wells Fargo ENT'],
       [5620, 'Brian Pressman', 3713, 'Wells Fargo ENT'],
       [5621, 'Aaron Hahn', 3713, 'Wells Fargo ENT'],
       [5622, 'Dana  Hamdan', 3713, 'Wells Fargo ENT'],
       [5623, 'Grace Jo', 3713, 'Wells Fargo ENT'],
       [5628, 'Andy Petrusky', 3713, 'Wells Fargo ENT'],
       [6357, 'Ashley Delapaz', 3713, 'Wells Fargo ENT']], dtype=object)

data = pd.read_csv(fileinput)
bdata = data[data['Visitor ID'].isin(l1)]
adata = data[data['Visitor ID'].isin(l2)]
b15 = bdata[bdata['Time on Site (minutes)'] <= 15].shape[0]
b30 = bdata[bdata['Time on Site (minutes)'].between(16, 30)].shape[0]
b60 = bdata[bdata['Time on Site (minutes)'].between(31, 60)].shape[0]
b90 = bdata[bdata['Time on Site (minutes)'].between(61, 90)].shape[0]
b120 = bdata[bdata['Time on Site (minutes)'].between(91, 151)].shape[0]
b150 = bdata[bdata['Time on Site (minutes)'].between(121, 150)].shape[0]
b151_plus = bdata[bdata['Time on Site (minutes)'] > 150].shape[0]

a15 = adata[adata['Time on Site (minutes)'] <= 15].shape[0]
a30 = adata[adata['Time on Site (minutes)'].between(16, 30)].shape[0]
a60 = adata[adata['Time on Site (minutes)'].between(31, 60)].shape[0]
a90 = adata[adata['Time on Site (minutes)'].between(61, 90)].shape[0]
a120 = adata[adata['Time on Site (minutes)'].between(91, 120)].shape[0]
a150 = adata[adata['Time on Site (minutes)'].between(121, 150)].shape[0]
a151_plus = adata[adata['Time on Site (minutes)'] > 150].shape[0]

at_abs = am_ugdata[am_ugdata[:, 2] == 43]
abs_list = at_abs[:, 0].tolist()
abs_out = data[data['Visitor ID'].isin(abs_list)]

at_crick = am_ugdata[am_ugdata[:, 2] == 2088]
crick_list = at_crick[:, 0].tolist()
crick_out = data[data['Visitor ID'].isin(crick_list)]

dorf = am_ugdata[am_ugdata[:, 2] == 24]
dorf_list = dorf[:, 0].tolist()
dorf_out = data[data['Visitor ID'].isin(dorf_list)]

at_loc = am_ugdata[am_ugdata[:, 2] == 3527]
loc_list = at_loc[:, 0].tolist()
loc_out = data[data['Visitor ID'].isin(loc_list)]

dtv = am_ugdata[am_ugdata[:, 2] == 3102]
dtv_list = dtv[:, 0].tolist()
dtv_out = data[data['Visitor ID'].isin(dtv_list)]


ido = am_ugdata[am_ugdata[:, 2] == 3169]
ido_list = dtv[:, 0].tolist()
ido_out = data[data['Visitor ID'].isin(ido_list)]



mb = am_ugdata[am_ugdata[:, 2] == 1083]
mb_list = mb[:, 0].tolist()
mb_out = data[data['Visitor ID'].isin(mb_list)]



sf = am_ugdata[np.isin(am_ugdata[:, 2], [3438, 25])]
sf_list = sf[:, 0].tolist()
sf_out = data[data['Visitor ID'].isin(sf_list)]


at_mob = am_ugdata[am_ugdata[:, 2] == 43]
at_mob_list = at_mob[:, 0].tolist()
mob_out = data[data['Visitor ID'].isin(at_mob_list)]

wf_cc = am_ugdata[am_ugdata[:, 2] == 46]
wf_cc_list = wf_cc[:, 0].tolist()
cc_out = data[data['Visitor ID'].isin(wf_cc_list)]

wf_ent = am_ugdata[am_ugdata[:, 2] == 3713]
wf_ent_list = wf_ent[:, 0].tolist()
ent_out = data[data['Visitor ID'].isin(wf_ent_list)]


print("Total Baseline Users: "  + str(bdata['Visitor ID'].count()))
print("Total Advanced Users: "  + str(adata['Visitor ID'].count()))
print("-------------------")
print("BASELINE")
print("Average Baseline TOP: "  + str(bdata['Time on Site (minutes)'].mean()))
print("Average Baseline DOP: "  + str(bdata['Days Active'].mean()))
print(" ")
print("Baseline Initiatives Launched: "  + str(bdata['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print("Baseline Initiatives Explored: "  + str(bdata['Clicks for Measure: Initiatives - Initiative | Open'].sum()))
print("Baseline Plans Run: "  + str(bdata['Clicks for Plan: New Plan - Run Plan'].sum()))
print("Baseline Plans Explored: "  + str(bdata['Clicks for Plan: Plans - Plan | Open'].sum()))
print("Baseline Buys Run: "  + str(bdata['Clicks for Buy: Plan Setup: Create Plan'].sum()))
print("Baseline Buys Explored: "  + str(bdata['Clicks for Buy: Investment Plans - Plan | Open'].sum()))
print(" ")
print("Baseline Users in MEASURE: "  + str(bdata[bdata['Time On Page (minutes) for Measure: BUCKET'] > 0].shape[0]))
print("Baseline Users in AUDIENCE: "  + str(bdata[bdata['Time On Page (minutes) for Audiences: BUCKET'] > 0].shape[0]))
print("Baseline Users in PLAN: "  + str(bdata[bdata['Time On Page (minutes) for Plan: BUCKET'] > 0].shape[0]))
print("Baseline Users in BUY: "  + str(bdata[bdata['Time On Page (minutes) for Buy: BUCKET'] > 0].shape[0]))
print(" ")
print("Baseline Users TOP Buckets 0-15: " + str(b15))
print("Baseline Users TOP Buckets 16-30: " + str(b30))
print("Baseline Users TOP Buckets 61-90: " + str(b60))
print("Baseline Users TOP Buckets 91-120: " + str(b90))
print("Baseline Users TOP Buckets 121-150: " + str(b120))
print("Baseline Users TOP Buckets 151-180: " + str(b150))
print("Baseline Users TOP Buckets 180+: " + str(b151_plus))
print("-------------------")
print("ADVANCED MEASUREMENT")
print("Average Advanced Measurement TOP: "  + str(adata['Time on Site (minutes)'].mean()))
print("Average Advanced Measurement DOP: "  + str(adata['Days Active'].mean()))
print(" ")
print("Advanced Measurement Initiatives Launched: "  + str(adata['Clicks for Measure: Initiative: Setup - Launch Initiative'].sum()))
print("Advanced Measurement Initiatives Explored: "  + str(adata['Clicks for Measure: Initiatives - Initiative | Open'].sum()))
print("Advanced Measurement Plans Run: "  + str(adata['Clicks for Plan: New Plan - Run Plan'].sum()))
print("Advanced Measurement Plans Explored: "  + str(adata['Clicks for Plan: Plans - Plan | Open'].sum()))
print("Advanced Measurement Buys Run: "  + str(adata['Clicks for Buy: Plan Setup: Create Plan'].sum()))
print("Advanced Measurement Buys Explored: "  + str(adata['Clicks for Buy: Investment Plans - Plan | Open'].sum()))
print(" ")
print("Advanced Measurement Users in MEASURE: "  + str(adata[adata['Time On Page (minutes) for Measure: BUCKET'] > 0].shape[0]))
print("Advanced Measurement Users in AUDIENCE: "  + str(adata[adata['Time On Page (minutes) for Audiences: BUCKET'] > 0].shape[0]))
print("Advanced Measurement Users in PLAN: "  + str(adata[adata['Time On Page (minutes) for Plan: BUCKET'] > 0].shape[0]))
print("Advanced Measurement Users in BUY: "  + str(adata[adata['Time On Page (minutes) for Buy: BUCKET'] > 0].shape[0]))
print(" ")
print("Advanced Measurement TOP Buckets 0-15: " + str(a15))
print("Advanced Measurement TOP Buckets 16-30: " + str(a30))
print("Advanced Measurement TOP Buckets 31-60: " + str(a60))
print("Advanced Measurement TOP Buckets 61-90: " + str(a90))
print("Advanced Measurement TOP Buckets 91-120: " + str(a120))
print("Advanced Measurement TOP Buckets 121-150: " + str(a150))
print("Advanced Measurement TOP Buckets 151+:  " + str(a151_plus))
print(" ")
print('(AM) AT&T ABS Users: ' + str(abs_out['Visitor ID'].shape[0]))
print('(AM) AT&T CRICKET Users: ' + str(crick_out['Visitor ID'].shape[0]))
print('(AM) AT&T Local Internet Users: ' + str(loc_out['Visitor ID'].shape[0]))
print('(AM) Beiersdorf Users: ' + str(dorf_out['Visitor ID'].shape[0]))
print('(AM) DIRECTV Users: ' + str(dtv_out['Visitor ID'].shape[0]))
print('(AM) IDORSIA Users: ' + str(ido_out['Visitor ID'].shape[0]))
print('(AM) MERCEDES BENZ Users: ' + str(mb_out['Visitor ID'].shape[0]))
print('(AM) STATE FARM Users: ' + str(sf_out['Visitor ID'].shape[0]))
print('(AM) AT&T MOBILITY Users: ' + str(mob_out['Visitor ID'].shape[0]))
print('(AM) Wells Fargo CC Users: ' + str(cc_out['Visitor ID'].shape[0]))
print('(AM) Wells Fargo ENT Users: ' + str(ent_out['Visitor ID'].shape[0]))