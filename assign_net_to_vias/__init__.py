try:

    from .assign_net_to_vias import AssignNetToVias

    AssignNetToVias().register()

except Exception as e:

    import os

    plugin_dir = os.path.dirname(os.path.realpath(__file__))
    log_file = os.path.join(plugin_dir, 'AssignNetToVias_error.log')

    with open(log_file, 'w') as f:
        f.write('>> ')
        f.write(repr(e))
