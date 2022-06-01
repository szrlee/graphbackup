
from src.rlpyt.rlpyt.utils.launching.affinity import encode_affinity
from src.rlpyt.rlpyt.utils.launching.exp_launcher import run_experiments
from src.rlpyt.rlpyt.utils.launching.variant import make_variants, VariantLevel

script = "rlpyt/experiments/scripts/atari/dqn/train/atari_r2d1_gpu.py"
affinity_code = encode_affinity(
    n_cpu_core=24,
    n_gpu=2,
    hyperthread_offset=24,
    n_socket=2,
)
runs_per_setting = 2
experiment_title = "atari_r2d1_long_4tr"
variant_levels = list()

games = ["gravitar"]
values = list(zip(games))
dir_names = ["{}".format(*v) for v in values]
keys = [("env", "game")]
variant_levels.append(VariantLevel(keys, values, dir_names))

variants, log_dirs = make_variants(*variant_levels)

default_config_key = "r2d1_long_4tr"

run_experiments(
    script=script,
    affinity_code=affinity_code,
    experiment_title=experiment_title,
    runs_per_setting=runs_per_setting,
    variants=variants,
    log_dirs=log_dirs,
    common_args=(default_config_key,),
)