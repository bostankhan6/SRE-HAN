def set_template(args):
    # Set the templates here
    #
    # if args.template.find('4X_SRE_HAN') >= 0:
    #     args.model = 'SRE_HAN_SIMD'
    #     args.n_resblocks = 20
    #     args.n_resgroups = 10
    #     args.patch_size = 192
    #     args.reduction = 4
    #     args.scale = "4"

        if args.template.find('8X_SRE_HAN') >= 0:
            args.model = 'SRE_HAN_SIMD'
            args.n_resblocks = 20
            args.n_resgroups = 10
            args.patch_size = 384
            args.reduction = 4
            args.scale = "8"

    # if args.template.find('HAN_SE_BLOCKX3') >= 0:
    #     args.model = 'HAN_SE_BLOCKX3'
    #     args.n_resblocks = 20
    #     args.n_resgroups = 10
    #     args.batch_size = 32
    #     args.patch_size = 192
    #     args.reduction = 4

    #X8
    # if args.template.find('HAN_SE_BLOCKX3_SINGLE_CONV_CA_SUM') >= 0:
    #     args.model = 'HAN_SE_BLOCKX3_SINGLE_CONV_CA_SUM'
    #     args.n_resblocks = 20
    #     args.n_resgroups = 10
    #     args.batch_size = 16
    #     args.patch_size = 384
    #     args.reduction = 4

    # if args.template.find('HAN') >= 0:
    #     args.model = 'HAN'
    #     args.n_resblocks = 20
    #     args.n_resgroups = 10
    #     args.batch_size = 32
    #     args.patch_size = 192

    #han_cowc_x4
    # if args.template.find('HAN_COWC') >= 0:
    #     args.model = 'HAN_COWC'
    #     args.n_resblocks = 20
    #     args.n_resgroups = 10
    #     args.batch_size = 32
    #     args.patch_size = 192

    # if args.template.find('SRE_HAN_COWC') >= 0:
    #     args.model = 'SRE_HAN_COWC'
    #     args.n_resblocks = 20
    #     args.n_resgroups = 10
    #     args.batch_size = 16
    #     args.patch_size = 384
    #     args.reduction = 4

    #X8
    # if args.template.find('HAN') >= 0:
    #     args.model = 'HAN'
    #     args.n_resblocks = 20
    #     args.n_resgroups = 10
    #     args.batch_size = 16
    #     args.patch_size = 384

    # if args.template.find('DRLN') >= 0:
    #     args.model = 'DRLN'
    #     args.batch_size = 32
    #     args.patch_size = 192
    #     args.reduction = 4