_base_ = [
    '../_base_/datasets/alfred-3d-class.py',
    '../_base_/models/votenet.py',
    '../_base_/default_runtime.py'
]
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=2
)
model = dict(
    backbone=dict(
        _delete_=True,
        type='Pointformer',
        num_points=(2048, 1024, 512, 256),
        radius=(0.2, 0.4, 0.8, 1.2),
        num_samples=(64, 32, 16, 16),
        basic_channels=64,
        fp_channels=((256, 256), (256, 256)),
        num_heads=8,
        num_layers=2,
        ratios=(1, 1, 1, 1),
        use_decoder=(False, False, False, False),
        use_lin_enc=False,
        cloud_points=20000,
        global_drop=0.2,
        decoder_drop=0.0,
        prenorm=False,
        norm_cfg=dict(type='BN2d')
    ),
    bbox_head=dict(
        num_classes=59,
        bbox_coder=dict(
            type='PartialBinBasedBBoxCoder',
            num_sizes=59,
            num_dir_bins=50,
            with_rot=True,
            mean_sizes=[
                [0.12661561956098577, 0.11136101362086785, 0.1079219900444433],
                [0.21102196236674797, 0.20753693413293528, 0.1019789830005446],
                [0.31632239127864026, 0.1900757409484316, 0.14473422938553201],
                [0.28399278193968897, 0.03544440599069651, 0.015264276277058113],
                [0.16329472606552914, 0.11602263625922296, 0.11293312524949457],
                [0.14303861617918842, 0.07803522206099252, 0.030212649395063542],
                [0.08602227736592108, 0.06389476274994042, 0.06229557089001548],
                [0.2537752448244552, 0.05060372474472313, 0.02698030433270614],
                [0.3413790118645063, 0.05252742822153418, 0.018010704892794892],
                [0.28660252781205825, 0.08814865797622998, 0.06036327953425369],
                [0.25590508367372616, 0.17582398545567574, 0.1691133379136104],
                [0.13139978445328604, 0.11298645821604991, 0.10600031002054937],
                [0.4213213002116291, 0.2723294541853888, 0.11249877975399648],
                [0.13627209040353408, 0.076868966373571, 0.07155040427973124],
                [0.25340960407266244, 0.24698951798066038, 0.19122716943427706],
                [0.12099201054155907, 0.08582502555609844, 0.08128412201363533],
                [0.3978943274824966, 0.2959819013322902, 0.16981993813812238],
                [0.13618160338448201, 0.07422126753641153, 0.0726738429105319],
                [0.24348057679134397, 0.1274734664404589, 0.10098703207345028],
                [0.30083676592288183, 0.06876014765308906, 0.022161196540282764],
                [0.21450201579223818, 0.04401493746695462, 0.024402741387560913],
                [0.1331215904835115, 0.12700013836600066, 0.10842944073094023],
                [0.4668359630882274, 0.4171362759099552, 0.34847899102377167],
                [0.08770314553045859, 0.055405696981320286, 0.007792009412307144],
                [0.13854349941934221, 0.06911846743986545, 0.01242089841061019],
                [0.40992979837796856, 0.3243551583529934, 0.311269741541903],
                [0.4697025818787984, 0.37309134486013795, 0.16007518550342126],
                [0.2230666551899201, 0.073841053464684, 0.026343099458033807],
                [0.3730822243835682, 0.2091065074209034, 0.16408680784477392],
                [0.22748524514579013, 0.1876331006176842, 0.16202517402106334],
                [0.14128478707032477, 0.04790679257742846, 0.047048292552338326],
                [0.23550951497873018, 0.18037485311928295, 0.04538026329566151],
                [0.4017351838751094, 0.12861736043872127, 0.037824672694450834],
                [0.5317533392159585, 0.15186709872107074, 0.1496175045945551],
                [0.48034804733971415, 0.14111124406128403, 0.13639411268733562],
                [0.09885843092757923, 0.0611968615743981, 0.031491936003610665],
                [0.2562606561656433, 0.1254965656538251, 0.04308236658124161],
                [0.12689792078596893, 0.11237793253346026, 0.10625091342835842],
                [0.5928475903614577, 0.45687944996279184, 0.048857577196310245],
                [0.32719614686024573, 0.15333164319262968, 0.03867626924579852],
                [0.08156687001873382, 0.05071685336550053, 0.038241874156451375],
                [0.3040537729453172, 0.2364882598568898, 0.04531965735075445],
                [0.16265015133147356, 0.08384107958841774, 0.013904400470479307],
                [0.27767184100185627, 0.19692194156711826, 0.1714101568696348],
                [0.26342439871155104, 0.1146303365896042, 0.11291343401926443],
                [0.21857064744847116, 0.08197182224326043, 0.06823181382949807],
                [0.355411177713587, 0.1040273429197989, 0.09653697451832666],
                [0.16704752836268835, 0.011955769069982148, 0.011388788463192292],
                [0.2146659417765231, 0.2112002990066247, 0.1897363649804095],
                [0.5350670943993971, 0.3018018412726604, 0.23432161606034715],
                [0.2113965528357545, 0.16182830884467003, 0.10380840522298632],
                [0.20252886898770966, 0.015305794292084202, 0.014635495275663234],
                [0.2124147621639316, 0.17544944648135033, 0.10768875224927033],
                [0.24608196400320062, 0.2434535118937522, 0.2433270103400917],
                [0.11295288923582156, 0.11223469214676471, 0.00489914003560398],
                [0.5051489337615382, 0.4777807617766836, 0.34413243977423746],
                [0.6687232732000341, 0.2743296823808269, 0.050819572264099847],
                [0.9737711123437103, 0.11382275090532776, 0.11230404033888296],
                [0.6042990518000055, 0.568448540000006, 0.5615892323999997],
            ]
        )
    )
)
optimizer = dict(type='AdamW', lr=3e-6, weight_decay=5e-2)
optimizer_config = dict(grad_clip=dict(max_norm=10, norm_type=2))
lr_config = dict(policy='step', warmup=None, step=[24, 32], gamma=0.3)
total_epochs = 30
workflow = [('train', 1)]
