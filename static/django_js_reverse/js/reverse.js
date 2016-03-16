this.Urls=(function(){var Urls={};var self={url_patterns:{}};var _get_url=function(url_pattern){return function(){var _arguments,index,url,url_arg,url_args,_i,_len,_ref,_ref_list,match_ref,provided_keys,build_kwargs;_arguments=arguments;_ref_list=self.url_patterns[url_pattern];if(arguments.length==1&&typeof(arguments[0])=="object"){var provided_keys_list=Object.keys(arguments[0]);provided_keys={};for(_i=0;_i<provided_keys_list.length;_i++)
provided_keys[provided_keys_list[_i]]=1;match_ref=function(ref)
{var _i;if(ref[1].length!=provided_keys_list.length)
return false;for(_i=0;_i<ref[1].length&&ref[1][_i]in provided_keys;_i++);return _i==ref[1].length;}
build_kwargs=function(keys){return _arguments[0];}}else{match_ref=function(ref)
{return ref[1].length==_arguments.length;}
build_kwargs=function(keys){var kwargs={};for(var i=0;i<keys.length;i++){kwargs[keys[i]]=_arguments[i];}
return kwargs;}}
for(_i=0;_i<_ref_list.length&&!match_ref(_ref_list[_i]);_i++);if(_i==_ref_list.length)
return null;_ref=_ref_list[_i];url=_ref[0],url_args=build_kwargs(_ref[1]);for(url_arg in url_args){url=url.replace("%("+url_arg+")s",url_args[url_arg]||'');}
return'/'+url;};};var name,pattern,self,url_patterns,_i,_len,_ref;url_patterns=[['admin\u002Duser\u002Dedit',[['member/user/edit/%(pk)s/',['pk',]]],],['admin:app_list',[['admin/%(app_label)s/',['app_label',]]],],['admin:auth_group_add',[['admin/auth/group/add/',[]]],],['admin:auth_group_change',[['admin/auth/group/%(_0)s/',['_0',]]],],['admin:auth_group_changelist',[['admin/auth/group/',[]]],],['admin:auth_group_delete',[['admin/auth/group/%(_0)s/delete/',['_0',]]],],['admin:auth_group_history',[['admin/auth/group/%(_0)s/history/',['_0',]]],],['admin:authtoken_token_add',[['admin/authtoken/token/add/',[]]],],['admin:authtoken_token_change',[['admin/authtoken/token/%(_0)s/',['_0',]]],],['admin:authtoken_token_changelist',[['admin/authtoken/token/',[]]],],['admin:authtoken_token_delete',[['admin/authtoken/token/%(_0)s/delete/',['_0',]]],],['admin:authtoken_token_history',[['admin/authtoken/token/%(_0)s/history/',['_0',]]],],['admin:customer_address_add',[['admin/customer/address/add/',[]]],],['admin:customer_address_change',[['admin/customer/address/%(_0)s/',['_0',]]],],['admin:customer_address_changelist',[['admin/customer/address/',[]]],],['admin:customer_address_delete',[['admin/customer/address/%(_0)s/delete/',['_0',]]],],['admin:customer_address_history',[['admin/customer/address/%(_0)s/history/',['_0',]]],],['admin:customer_customer_add',[['admin/customer/customer/add/',[]]],],['admin:customer_customer_change',[['admin/customer/customer/%(_0)s/',['_0',]]],],['admin:customer_customer_changelist',[['admin/customer/customer/',[]]],],['admin:customer_customer_delete',[['admin/customer/customer/%(_0)s/delete/',['_0',]]],],['admin:customer_customer_history',[['admin/customer/customer/%(_0)s/history/',['_0',]]],],['admin:customer_interesttag_add',[['admin/customer/interesttag/add/',[]]],],['admin:customer_interesttag_change',[['admin/customer/interesttag/%(_0)s/',['_0',]]],],['admin:customer_interesttag_changelist',[['admin/customer/interesttag/',[]]],],['admin:customer_interesttag_delete',[['admin/customer/interesttag/%(_0)s/delete/',['_0',]]],],['admin:customer_interesttag_history',[['admin/customer/interesttag/%(_0)s/history/',['_0',]]],],['admin:djcelery_crontabschedule_add',[['admin/djcelery/crontabschedule/add/',[]]],],['admin:djcelery_crontabschedule_change',[['admin/djcelery/crontabschedule/%(_0)s/',['_0',]]],],['admin:djcelery_crontabschedule_changelist',[['admin/djcelery/crontabschedule/',[]]],],['admin:djcelery_crontabschedule_delete',[['admin/djcelery/crontabschedule/%(_0)s/delete/',['_0',]]],],['admin:djcelery_crontabschedule_history',[['admin/djcelery/crontabschedule/%(_0)s/history/',['_0',]]],],['admin:djcelery_intervalschedule_add',[['admin/djcelery/intervalschedule/add/',[]]],],['admin:djcelery_intervalschedule_change',[['admin/djcelery/intervalschedule/%(_0)s/',['_0',]]],],['admin:djcelery_intervalschedule_changelist',[['admin/djcelery/intervalschedule/',[]]],],['admin:djcelery_intervalschedule_delete',[['admin/djcelery/intervalschedule/%(_0)s/delete/',['_0',]]],],['admin:djcelery_intervalschedule_history',[['admin/djcelery/intervalschedule/%(_0)s/history/',['_0',]]],],['admin:djcelery_periodictask_add',[['admin/djcelery/periodictask/add/',[]]],],['admin:djcelery_periodictask_change',[['admin/djcelery/periodictask/%(_0)s/',['_0',]]],],['admin:djcelery_periodictask_changelist',[['admin/djcelery/periodictask/',[]]],],['admin:djcelery_periodictask_delete',[['admin/djcelery/periodictask/%(_0)s/delete/',['_0',]]],],['admin:djcelery_periodictask_history',[['admin/djcelery/periodictask/%(_0)s/history/',['_0',]]],],['admin:djcelery_taskstate_add',[['admin/djcelery/taskstate/add/',[]]],],['admin:djcelery_taskstate_change',[['admin/djcelery/taskstate/%(_0)s/',['_0',]]],],['admin:djcelery_taskstate_changelist',[['admin/djcelery/taskstate/',[]]],],['admin:djcelery_taskstate_delete',[['admin/djcelery/taskstate/%(_0)s/delete/',['_0',]]],],['admin:djcelery_taskstate_history',[['admin/djcelery/taskstate/%(_0)s/history/',['_0',]]],],['admin:djcelery_workerstate_add',[['admin/djcelery/workerstate/add/',[]]],],['admin:djcelery_workerstate_change',[['admin/djcelery/workerstate/%(_0)s/',['_0',]]],],['admin:djcelery_workerstate_changelist',[['admin/djcelery/workerstate/',[]]],],['admin:djcelery_workerstate_delete',[['admin/djcelery/workerstate/%(_0)s/delete/',['_0',]]],],['admin:djcelery_workerstate_history',[['admin/djcelery/workerstate/%(_0)s/history/',['_0',]]],],['admin:express_expresscarrier_add',[['admin/express/expresscarrier/add/',[]]],],['admin:express_expresscarrier_change',[['admin/express/expresscarrier/%(_0)s/',['_0',]]],],['admin:express_expresscarrier_changelist',[['admin/express/expresscarrier/',[]]],],['admin:express_expresscarrier_delete',[['admin/express/expresscarrier/%(_0)s/delete/',['_0',]]],],['admin:express_expresscarrier_history',[['admin/express/expresscarrier/%(_0)s/history/',['_0',]]],],['admin:express_expressorder_add',[['admin/express/expressorder/add/',[]]],],['admin:express_expressorder_change',[['admin/express/expressorder/%(_0)s/',['_0',]]],],['admin:express_expressorder_changelist',[['admin/express/expressorder/',[]]],],['admin:express_expressorder_delete',[['admin/express/expressorder/%(_0)s/delete/',['_0',]]],],['admin:express_expressorder_history',[['admin/express/expressorder/%(_0)s/history/',['_0',]]],],['admin:index',[['admin/',[]]],],['admin:jsi18n',[['admin/jsi18n/',[]]],],['admin:login',[['admin/login/',[]]],],['admin:logout',[['admin/logout/',[]]],],['admin:member_seller_add',[['admin/member/seller/add/',[]]],],['admin:member_seller_change',[['admin/member/seller/%(_0)s/',['_0',]]],],['admin:member_seller_changelist',[['admin/member/seller/',[]]],],['admin:member_seller_delete',[['admin/member/seller/%(_0)s/delete/',['_0',]]],],['admin:member_seller_history',[['admin/member/seller/%(_0)s/history/',['_0',]]],],['admin:messageset_notification_add',[['admin/messageset/notification/add/',[]]],],['admin:messageset_notification_change',[['admin/messageset/notification/%(_0)s/',['_0',]]],],['admin:messageset_notification_changelist',[['admin/messageset/notification/',[]]],],['admin:messageset_notification_delete',[['admin/messageset/notification/%(_0)s/delete/',['_0',]]],],['admin:messageset_notification_history',[['admin/messageset/notification/%(_0)s/history/',['_0',]]],],['admin:messageset_notificationcontent_add',[['admin/messageset/notificationcontent/add/',[]]],],['admin:messageset_notificationcontent_change',[['admin/messageset/notificationcontent/%(_0)s/',['_0',]]],],['admin:messageset_notificationcontent_changelist',[['admin/messageset/notificationcontent/',[]]],],['admin:messageset_notificationcontent_delete',[['admin/messageset/notificationcontent/%(_0)s/delete/',['_0',]]],],['admin:messageset_notificationcontent_history',[['admin/messageset/notificationcontent/%(_0)s/history/',['_0',]]],],['admin:messageset_sitemailcontent_add',[['admin/messageset/sitemailcontent/add/',[]]],],['admin:messageset_sitemailcontent_change',[['admin/messageset/sitemailcontent/%(_0)s/',['_0',]]],],['admin:messageset_sitemailcontent_changelist',[['admin/messageset/sitemailcontent/',[]]],],['admin:messageset_sitemailcontent_delete',[['admin/messageset/sitemailcontent/%(_0)s/delete/',['_0',]]],],['admin:messageset_sitemailcontent_history',[['admin/messageset/sitemailcontent/%(_0)s/history/',['_0',]]],],['admin:messageset_sitemailreceive_add',[['admin/messageset/sitemailreceive/add/',[]]],],['admin:messageset_sitemailreceive_change',[['admin/messageset/sitemailreceive/%(_0)s/',['_0',]]],],['admin:messageset_sitemailreceive_changelist',[['admin/messageset/sitemailreceive/',[]]],],['admin:messageset_sitemailreceive_delete',[['admin/messageset/sitemailreceive/%(_0)s/delete/',['_0',]]],],['admin:messageset_sitemailreceive_history',[['admin/messageset/sitemailreceive/%(_0)s/history/',['_0',]]],],['admin:messageset_sitemailsend_add',[['admin/messageset/sitemailsend/add/',[]]],],['admin:messageset_sitemailsend_change',[['admin/messageset/sitemailsend/%(_0)s/',['_0',]]],],['admin:messageset_sitemailsend_changelist',[['admin/messageset/sitemailsend/',[]]],],['admin:messageset_sitemailsend_delete',[['admin/messageset/sitemailsend/%(_0)s/delete/',['_0',]]],],['admin:messageset_sitemailsend_history',[['admin/messageset/sitemailsend/%(_0)s/history/',['_0',]]],],['admin:messageset_task_add',[['admin/messageset/task/add/',[]]],],['admin:messageset_task_change',[['admin/messageset/task/%(_0)s/',['_0',]]],],['admin:messageset_task_changelist',[['admin/messageset/task/',[]]],],['admin:messageset_task_delete',[['admin/messageset/task/%(_0)s/delete/',['_0',]]],],['admin:messageset_task_history',[['admin/messageset/task/%(_0)s/history/',['_0',]]],],['admin:order_order_add',[['admin/order/order/add/',[]]],],['admin:order_order_change',[['admin/order/order/%(_0)s/',['_0',]]],],['admin:order_order_changelist',[['admin/order/order/',[]]],],['admin:order_order_delete',[['admin/order/order/%(_0)s/delete/',['_0',]]],],['admin:order_order_history',[['admin/order/order/%(_0)s/history/',['_0',]]],],['admin:order_orderproduct_add',[['admin/order/orderproduct/add/',[]]],],['admin:order_orderproduct_change',[['admin/order/orderproduct/%(_0)s/',['_0',]]],],['admin:order_orderproduct_changelist',[['admin/order/orderproduct/',[]]],],['admin:order_orderproduct_delete',[['admin/order/orderproduct/%(_0)s/delete/',['_0',]]],],['admin:order_orderproduct_history',[['admin/order/orderproduct/%(_0)s/history/',['_0',]]],],['admin:password_change',[['admin/password_change/',[]]],],['admin:password_change_done',[['admin/password_change/done/',[]]],],['admin:product_brand_add',[['admin/product/brand/add/',[]]],],['admin:product_brand_change',[['admin/product/brand/%(_0)s/',['_0',]]],],['admin:product_brand_changelist',[['admin/product/brand/',[]]],],['admin:product_brand_delete',[['admin/product/brand/%(_0)s/delete/',['_0',]]],],['admin:product_brand_history',[['admin/product/brand/%(_0)s/history/',['_0',]]],],['admin:product_category_add',[['admin/product/category/add/',[]]],],['admin:product_category_change',[['admin/product/category/%(_0)s/',['_0',]]],],['admin:product_category_changelist',[['admin/product/category/',[]]],],['admin:product_category_delete',[['admin/product/category/%(_0)s/delete/',['_0',]]],],['admin:product_category_history',[['admin/product/category/%(_0)s/history/',['_0',]]],],['admin:product_country_add',[['admin/product/country/add/',[]]],],['admin:product_country_change',[['admin/product/country/%(_0)s/',['_0',]]],],['admin:product_country_changelist',[['admin/product/country/',[]]],],['admin:product_country_delete',[['admin/product/country/%(_0)s/delete/',['_0',]]],],['admin:product_country_history',[['admin/product/country/%(_0)s/history/',['_0',]]],],['admin:product_product_add',[['admin/product/product/add/',[]]],],['admin:product_product_change',[['admin/product/product/%(_0)s/',['_0',]]],],['admin:product_product_changelist',[['admin/product/product/',[]]],],['admin:product_product_delete',[['admin/product/product/%(_0)s/delete/',['_0',]]],],['admin:product_product_history',[['admin/product/product/%(_0)s/history/',['_0',]]],],['admin:report_monthlyreport_add',[['admin/report/monthlyreport/add/',[]]],],['admin:report_monthlyreport_change',[['admin/report/monthlyreport/%(_0)s/',['_0',]]],],['admin:report_monthlyreport_changelist',[['admin/report/monthlyreport/',[]]],],['admin:report_monthlyreport_delete',[['admin/report/monthlyreport/%(_0)s/delete/',['_0',]]],],['admin:report_monthlyreport_history',[['admin/report/monthlyreport/%(_0)s/history/',['_0',]]],],['admin:store_page_add',[['admin/store/page/add/',[]]],],['admin:store_page_change',[['admin/store/page/%(_0)s/',['_0',]]],],['admin:store_page_changelist',[['admin/store/page/',[]]],],['admin:store_page_delete',[['admin/store/page/%(_0)s/delete/',['_0',]]],],['admin:store_page_history',[['admin/store/page/%(_0)s/history/',['_0',]]],],['admin:store_store_add',[['admin/store/store/add/',[]]],],['admin:store_store_change',[['admin/store/store/%(_0)s/',['_0',]]],],['admin:store_store_changelist',[['admin/store/store/',[]]],],['admin:store_store_delete',[['admin/store/store/%(_0)s/delete/',['_0',]]],],['admin:store_store_history',[['admin/store/store/%(_0)s/history/',['_0',]]],],['admin:taggit_tag_add',[['admin/taggit/tag/add/',[]]],],['admin:taggit_tag_change',[['admin/taggit/tag/%(_0)s/',['_0',]]],],['admin:taggit_tag_changelist',[['admin/taggit/tag/',[]]],],['admin:taggit_tag_delete',[['admin/taggit/tag/%(_0)s/delete/',['_0',]]],],['admin:taggit_tag_history',[['admin/taggit/tag/%(_0)s/history/',['_0',]]],],['admin:view_on_site',[['admin/r/%(content_type_id)s/%(object_id)s/',['content_type_id','object_id',]]],],['adminlte:common_create_page',[['common/%(app_name)s/%(model_name)s/create/',['app_name','model_name',]]],],['adminlte:common_delete_page',[['common/%(app_name)s/%(model_name)s/delete/',['app_name','model_name',]]],],['adminlte:common_detail_page',[['common/%(app_name)s/%(model_name)s/detail/%(pk)s/',['app_name','model_name','pk',]]],],['adminlte:common_list_page',[['common/%(app_name)s/%(model_name)s/list/',['app_name','model_name',]]],],['adminlte:common_update_page',[['common/%(app_name)s/%(model_name)s/update/%(pk)s/',['app_name','model_name','pk',]]],],['adminlte:http403',[['/403.html',[]]],],['api:api\u002Dproduct\u002Ddetail',[['api/product/product/%(pk)s/.%(format)s',['pk','format',],],['api/product/product/%(pk)s/',['pk',]]],],['api:api\u002Dproduct\u002Dlist',[['api/product/product/.%(format)s',['format',],],['api/product/product/',[]]],],['api:customer\u002Ddetail',[['api/customer/customer/%(pk)s/.%(format)s',['pk','format',],],['api/customer/customer/%(pk)s/',['pk',]]],],['api:customer\u002Dlist',[['api/customer/customer/.%(format)s',['format',],],['api/customer/customer/',[]]],],['api:groups\u002Dand\u002Dusers',[['api/member/groups_and_users/',[]]],],['api:login\u002Dtoken',[['api/member/api\u002Dtoken\u002Dauth/',[]]],],['api:order\u002Ddetail',[['api/order/order/%(pk)s/.%(format)s',['pk','format',],],['api/order/order/%(pk)s/',['pk',]]],],['api:order\u002Dlist',[['api/order/order/.%(format)s',['format',],],['api/order/order/',[]]],],['api:profile',[['api/member/profile/',[]]],],['api:user\u002Ddetail',[['api/member/user/%(pk)s/.%(format)s',['pk','format',],],['api/member/user/%(pk)s/',['pk',]]],],['api:user\u002Dlist',[['api/member/user/.%(format)s',['format',],],['api/member/user/',[]]],],['app_settings',[['admin/settings/%(app_label)s/',['app_label',]]],],['change_password',[['auth/change\u002Dpassword/',[]]],],['common_api:listcreate_api',[['api/v1/%(app_name)s/%(model_name)s/',['app_name','model_name',]]],],['common_api:retriveupdate_api',[['api/v1/%(app_name)s/%(model_name)s/%(pk)s',['app_name','model_name','pk',]]],],['customer\u002Dadd',[['customer/add/',[]]],],['customer\u002Dadd\u002Dview',[['customer/customer/add/',[]]],],['customer\u002Ddelete\u002Dview',[['customer/customer/delete/',[]]],],['customer\u002Ddetail\u002Dview',[['customer/customer/%(pk)s/',['pk',]]],],['customer\u002Dedit',[['customer/edit/%(pk)s/',['pk',]]],],['customer\u002Dlist',[['customer/',[]]],],['customer\u002Dlist\u002Dview',[['customer/customer/list/',[]]],],['customer\u002Dupdate\u002Dview',[['customer/customer/%(pk)s/edit/',['pk',]]],],['js_reverse',[['jsreverse/',[]]],],['member\u002Dhome',[['member/home/',[]]],],['member\u002Dlogin',[['member/login/',[]]],],['member\u002Dlogout',[['member/logout/',[]]],],['member\u002Dprofile',[['member/profile/',[]]],],['messageset:api\u002Dnotification\u002Ddelete',[['api/messageset/notification/delete/.%(format)s',['format',],],['api/messageset/notification/delete/',[]]],],['messageset:api\u002Dnotification\u002Ddetail',[['api/messageset/notification/%(pk)s/.%(format)s',['pk','format',],],['api/messageset/notification/%(pk)s/',['pk',]]],],['messageset:api\u002Dnotification\u002Dlist',[['api/messageset/notification/.%(format)s',['format',],],['api/messageset/notification/',[]]],],['messageset:api\u002Dnotification\u002Dpage',[['api/messageset/notification/page/.%(format)s',['format',],],['api/messageset/notification/page/',[]]],],['messageset:api\u002Dnotificationcontent\u002Ddelete',[['api/messageset/notificationcontent/delete/.%(format)s',['format',],],['api/messageset/notificationcontent/delete/',[]]],],['messageset:api\u002Dnotificationcontent\u002Ddetail',[['api/messageset/notificationcontent/%(pk)s/.%(format)s',['pk','format',],],['api/messageset/notificationcontent/%(pk)s/',['pk',]]],],['messageset:api\u002Dnotificationcontent\u002Dlist',[['api/messageset/notificationcontent/.%(format)s',['format',],],['api/messageset/notificationcontent/',[]]],],['messageset:api\u002Dnotificationcontent\u002Dpage',[['api/messageset/notificationcontent/page/.%(format)s',['format',],],['api/messageset/notificationcontent/page/',[]]],],['messageset:api\u002Dsitemail_markall',[['api/messageset/sitemail/receive/markall',[]]],],['messageset:api\u002Dsitemailcontent\u002Ddelete',[['api/messageset/sitemailcontent/delete/.%(format)s',['format',],],['api/messageset/sitemailcontent/delete/',[]]],],['messageset:api\u002Dsitemailcontent\u002Ddetail',[['api/messageset/sitemailcontent/%(pk)s/.%(format)s',['pk','format',],],['api/messageset/sitemailcontent/%(pk)s/',['pk',]]],],['messageset:api\u002Dsitemailcontent\u002Dlist',[['api/messageset/sitemailcontent/.%(format)s',['format',],],['api/messageset/sitemailcontent/',[]]],],['messageset:api\u002Dsitemailcontent\u002Dpage',[['api/messageset/sitemailcontent/page/.%(format)s',['format',],],['api/messageset/sitemailcontent/page/',[]]],],['messageset:api\u002Dsitemailreceive\u002Ddelete',[['api/messageset/sitemailreceive/delete/.%(format)s',['format',],],['api/messageset/sitemailreceive/delete/',[]]],],['messageset:api\u002Dsitemailreceive\u002Ddetail',[['api/messageset/sitemailreceive/%(pk)s/.%(format)s',['pk','format',],],['api/messageset/sitemailreceive/%(pk)s/',['pk',]]],],['messageset:api\u002Dsitemailreceive\u002Dlist',[['api/messageset/sitemailreceive/.%(format)s',['format',],],['api/messageset/sitemailreceive/',[]]],],['messageset:api\u002Dsitemailreceive\u002Dpage',[['api/messageset/sitemailreceive/page/.%(format)s',['format',],],['api/messageset/sitemailreceive/page/',[]]],],['messageset:api\u002Dsitemailsend\u002Ddelete',[['api/messageset/sitemailsend/delete/.%(format)s',['format',],],['api/messageset/sitemailsend/delete/',[]]],],['messageset:api\u002Dsitemailsend\u002Ddetail',[['api/messageset/sitemailsend/%(pk)s/.%(format)s',['pk','format',],],['api/messageset/sitemailsend/%(pk)s/',['pk',]]],],['messageset:api\u002Dsitemailsend\u002Dlist',[['api/messageset/sitemailsend/.%(format)s',['format',],],['api/messageset/sitemailsend/',[]]],],['messageset:api\u002Dsitemailsend\u002Dpage',[['api/messageset/sitemailsend/page/.%(format)s',['format',],],['api/messageset/sitemailsend/page/',[]]],],['messageset:api\u002Dtask\u002Ddelete',[['api/messageset/task/delete/.%(format)s',['format',],],['api/messageset/task/delete/',[]]],],['messageset:api\u002Dtask\u002Ddetail',[['api/messageset/task/%(pk)s/.%(format)s',['pk','format',],],['api/messageset/task/%(pk)s/',['pk',]]],],['messageset:api\u002Dtask\u002Dlist',[['api/messageset/task/.%(format)s',['format',],],['api/messageset/task/',[]]],],['messageset:api\u002Dtask\u002Dpage',[['api/messageset/task/page/.%(format)s',['format',],],['api/messageset/task/page/',[]]],],['messageset:notification\u002Ddetail',[['messageset/notification/%(pk)s/',['pk',]]],],['messageset:notification\u002Dlist',[['messageset/notification/list/',[]]],],['messageset:notification\u002Dupdate',[['messageset/notification/%(pk)s/edit/',['pk',]]],],['messageset:notificationcontent\u002Dadd',[['messageset/notificationcontent/add/',[]]],],['messageset:notificationcontent\u002Ddetail',[['messageset/notificationcontent/%(pk)s/',['pk',]]],],['messageset:notificationcontent\u002Dupdate',[['messageset/notificationcontent/%(pk)s/edit/',['pk',]]],],['messageset:sitemail\u002Dadd',[['messageset/sitemail/add/',[]]],],['messageset:sitemail\u002Dlist',[['messageset/sitemail/list/',[]]],],['messageset:sitemailcontent\u002Ddetail',[['messageset/sitemailcontent/%(pk)s/',['pk',]]],],['messageset:sitemailcontent\u002Dupdate',[['messageset/sitemailcontent/%(pk)s/edit/',['pk',]]],],['messageset:sitemailreceive\u002Ddetail',[['messageset/sitemail/receive/%(pk)s/',['pk',]]],],['messageset:sitemailsend\u002Ddetail',[['messageset/sitemailsend/%(pk)s/',['pk',]]],],['messageset:task\u002Ddetail',[['messageset/task/%(pk)s/',['pk',]]],],['messageset:task\u002Dlist',[['messageset/task/list/',[]]],],['order:api\u002Dorder\u002Ddelete',[['api/order/order/delete/.%(format)s',['format',],],['api/order/order/delete/',[]]],],['order:api\u002Dorder\u002Ddetail',[['api/order/order/%(pk)s/.%(format)s',['pk','format',],],['api/order/order/%(pk)s/',['pk',]]],],['order:api\u002Dorder\u002Dlist',[['api/order/order/.%(format)s',['format',],],['api/order/order/',[]]],],['order:api\u002Dorder\u002Dpage',[['api/order/order/page/.%(format)s',['format',],],['api/order/order/page/',[]]],],['order:change\u002Dorder\u002Dpaid',[['order/paid/%(order_id)s/',['order_id',]]],],['order:change\u002Dorder\u002Dstatus',[['order/%(order_id)s/status/%(status_value)s/',['order_id','status_value',]]],],['order:order\u002Dadd',[['order/add/',[]]],],['order:order\u002Ddetail',[['order/%(customer_id)s/%(pk)s/',['customer_id','pk',]]],],['order:order\u002Ddetail\u002Dshort',[['%(customer_id)s/%(pk)s/',['customer_id','pk',]]],],['order:order\u002Dindex',[['order/index/',[]]],],['order:order\u002Dlist',[['order/list/',[]]],],['order:order\u002Dlist\u002Dshort',[['order/',[]]],],['order:order\u002Dupdate',[['order/%(pk)s/edit/',['pk',]]],],['password_change_done',[['auth/change\u002Dpassword\u002Ddone/',[]]],],['password_reset_complete',[['member/password/reset/complete/',[]]],],['password_reset_done',[['member/password/reset/done/',[]]],],['product:api\u002Dbrand\u002Ddelete',[['api/product/brand/delete/.%(format)s',['format',],],['api/product/brand/delete/',[]]],],['product:api\u002Dbrand\u002Ddetail',[['api/product/brand/%(pk)s/.%(format)s',['pk','format',],],['api/product/brand/%(pk)s/',['pk',]]],],['product:api\u002Dbrand\u002Dlist',[['api/product/brand/.%(format)s',['format',],],['api/product/brand/',[]]],],['product:api\u002Dbrand\u002Dpage',[['api/product/brand/page/.%(format)s',['format',],],['api/product/brand/page/',[]]],],['product:api\u002Dproduct\u002Ddelete',[['api/product/product/delete/.%(format)s',['format',],],['api/product/product/delete/',[]]],],['product:api\u002Dproduct\u002Ddetail',[['api/product/product/%(pk)s/.%(format)s',['pk','format',],],['api/product/product/%(pk)s/',['pk',]]],],['product:api\u002Dproduct\u002Dlist',[['api/product/product/.%(format)s',['format',],],['api/product/product/',[]]],],['product:api\u002Dproduct\u002Dpage',[['api/product/product/page/.%(format)s',['format',],],['api/product/product/page/',[]]],],['product:brand\u002Dadd',[['product/brand/add/',[]]],],['product:brand\u002Ddetail',[['product/brand/%(pk)s/',['pk',]]],],['product:brand\u002Dlist',[['product/brand/list/',[]]],],['product:brand\u002Dupdate',[['product/brand/%(pk)s/edit/',['pk',]]],],['product:product\u002Dadd',[['product/add/',[]]],],['product:product\u002Dadd\u002Dview',[['product/product/add/',[]]],],['product:product\u002Ddetail',[['product/product/%(pk)s/',['pk',]]],],['product:product\u002Dedit',[['product/edit/%(pk)s/',['pk',]]],],['product:product\u002Dlist',[['product/',[]]],],['product:product\u002Dlist\u002Dview',[['product/product/list/',[]]],],['product:product\u002Dupdate',[['product/product/%(pk)s/edit/',['pk',]]],],['registration:login',[['auth/login/',[]]],],['registration:logout',[['auth/logout/',[]]],],['registration:register',[['auth/register/',[]]],],['seller\u002Dadd',[['member/user/add/',[]]],],['seller\u002Dindex',[['member/users/',[]]],],['site_settings',[['admin/settings/',[]]],],['store:api\u002Dpage\u002Ddelete',[['api/store/page/delete/.%(format)s',['format',],],['api/store/page/delete/',[]]],],['store:api\u002Dpage\u002Ddetail',[['api/store/page/%(pk)s/.%(format)s',['pk','format',],],['api/store/page/%(pk)s/',['pk',]]],],['store:api\u002Dpage\u002Dlist',[['api/store/page/.%(format)s',['format',],],['api/store/page/',[]]],],['store:api\u002Dpage\u002Dpage',[['api/store/page/page/.%(format)s',['format',],],['api/store/page/page/',[]]],],['store:api\u002Dstore\u002Ddelete',[['api/store/store/delete/.%(format)s',['format',],],['api/store/store/delete/',[]]],],['store:api\u002Dstore\u002Ddetail',[['api/store/store/%(pk)s/.%(format)s',['pk','format',],],['api/store/store/%(pk)s/',['pk',]]],],['store:api\u002Dstore\u002Dlist',[['api/store/store/.%(format)s',['format',],],['api/store/store/',[]]],],['store:api\u002Dstore\u002Dpage',[['api/store/store/page/.%(format)s',['format',],],['api/store/store/page/',[]]],],['store:page\u002Dadd',[['store/page/add/',[]]],],['store:page\u002Ddetail',[['store/page/%(pk)s/',['pk',]]],],['store:page\u002Dlist',[['store/page/list/',[]]],],['store:page\u002Dupdate',[['store/page/%(pk)s/edit/',['pk',]]],],['store:store\u002Dadd',[['store/store/add/',[]]],],['store:store\u002Ddetail',[['store/store/%(pk)s/',['pk',]]],],['store:store\u002Dlist',[['store/store/list/',[]]],],['store:store\u002Dupdate',[['store/store/%(pk)s/edit/',['pk',]]],],['user\u002Ddelete',[['member/user/delete/%(pk)s/',['pk',]]],],['user\u002Dpassword',[['member/user/password/%(pk)s/',['pk',]]]]];self.url_patterns={};for(_i=0,_len=url_patterns.length;_i<_len;_i++){_ref=url_patterns[_i],name=_ref[0],pattern=_ref[1];self.url_patterns[name]=pattern;Urls[name]=_get_url(name);Urls[name.replace(/-/g,'_')]=_get_url(name);}
return Urls;})();