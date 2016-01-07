import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def groups():
    # Return a list of groups
    return toolkit.get_action('group_list')(data_dict={'all_fields': True})

def dataset_count():
    # Return a count of all datasets
    result = toolkit.get_action('package_search')(data_dict={'rows': 1})
    return result['count']

class CobPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'cob')

    def get_helpers(self):
        # Register cob_theme_* helper functions
        return {'cob_theme_groups': groups,
            'cob_theme_dataset_count': dataset_count}
