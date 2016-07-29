
var brandListPageVue = new CommonListPageVue({
        data: {
            // API
            list_api_tag:   'product:api-brand-list',
            detail_api_tag: 'product:api-brand-detail',
            delete_api_tag: 'product:api-brand-delete',
            // page
            create_url_tag: 'product:brand-add',
            list_url_tag:   'product:brand-list',
            update_url_tag: 'product:brand-update',
            detail_url_tag: 'product:brand-detail',
            list_url:       Urls['product:api-brand-list']()
        }
    }
);
