import matplotlib.pyplot as plt
import numpy as np

PATH = '../Text/images/results/'


PCK = {
    "name": "PCK",

    "LSP": {
        "BlasePose": [0.728, 0.931, 0.978],
        "MoveNet": [0.356, 0.928, 0.983],
        "OpenPose": [0.708, 0.837, 0.882],
        "MMPose": [0.728, 0.85, 0.914],
    },

    "LSPE": {
        "BlasePose": [0.454, 0.743, 0.825],
        "MoveNet": [0.144, 0.539, 0.745],
        "OpenPose": [0.362, 0.524, 0.633],
        "MMPose": [0.403, 0.56, 0.651],
    },

    "Halpe": {
        "BlasePose": [0.365, 0.519, 0.595],
        "MoveNet": [0.04, 0.052, 0.223],
        "OpenPose": [0.575, 0.638, 0.686],
        "MMPose": [0.424, 0.483, 0.537],
    },
}



PDJ = {
    "name": "PDJ",

    "LSP": {
        "BlasePose": [0.773, 0.944, 0.988],
        "MoveNet": [0.43, 0.95, 0.993],
        "OpenPose": [0.746, 0.845, 0.899],
        "MMPose": [0.76, 0.858, 0.933],
    },

    "LSPE": {
        "BlasePose": [0.557, 0.783, 0.851],
        "MoveNet": [0.227, 0.635, 0.806],
        "OpenPose": [0.42, 0.569, 0.69],
        "MMPose": [0.463, 0.587, 0.72],
    },

    "Halpe": {
        "BlasePose": [0.417, 0.554, 0.638],
        "MoveNet": [0.006, 0.078, 0.32],
        "OpenPose": [0.613, 0.658, 0.72],
        "MMPose": [0.456, 0.502, 0.578],
    },
}



AP = {
    "name": "AP",

    "LSP": {
        "BlasePose": [0.184, 0.093, 0.1],
        "MoveNet": [0.168, 0.064, 0.08],
        "OpenPose": [0.166, 0.085, 0.092],
        "MMPose": [0.225, 0.223, 0.123],
    },

    "LSPE": {
        "BlasePose": [0.675, 0.457, 0.443],
        "MoveNet": [0.312, 0.059, 0.111],
        "OpenPose": [0.538, 0.362, 0.362],
        "MMPose": [0.598, 0.462, 0.443],
    },

    "Halpe": {
        "BlasePose": [0.33, 0.158, 0.173],
        "MoveNet": [0, 0, 0],
        "OpenPose": [0.562, 0.398, 0.384],
        "MMPose": [0.661, 0.544, 0.512],
    },
}

colors = {
    "BlasePose": 'r',
    "MoveNet": 'g',
    "OpenPose": 'b',
    "MMPose": 'y',
}


for metric in [PCK, PDJ, AP]:
    if metric == AP:
        x = ["0.5", "0.75", "0.5 : 0.95 : 0.05"]
        loc = 1
    else:
        x = ["0.05", "0.2", "0.5"]
        loc = 2

    for dataset in ["LSP", "LSPE", "Halpe"]:
        fig, ax = plt.subplots()
        for model in ["BlasePose", "MoveNet", "OpenPose", "MMPose"]:
            ax.plot(x, metric[dataset][model], color=colors[model], label=model)
        
        ax.legend(
            loc=loc,
            fontsize = 12,
        )
        fig.set_figheight(4)
        fig.set_figwidth(10)

        ax.set_xlabel("Значение порога для метрики")
        ax.set_ylabel("Значение метрики")

        plt.savefig(PATH + f"{metric['name']}_{dataset}.png", bbox_inches='tight')



    fig, ax = plt.subplots()

    for model in ["BlasePose", "MoveNet", "OpenPose", "MMPose"]:
        values = np.zeros(3)
        for dataset in ["LSP", "LSPE", "Halpe"]:
            values = values + np.array(metric[dataset][model])
        
        values = values / 4
        ax.plot(x, values, color=colors[model], label=model)

    ax.legend(
            loc=loc,
            fontsize = 12,
        )
    fig.set_figheight(4)
    fig.set_figwidth(10)

    ax.set_xlabel("Значение порога для метрики")
    ax.set_ylabel("Значение метрики")

    plt.savefig(PATH + f"{metric['name']}.png", bbox_inches='tight')

            
    

