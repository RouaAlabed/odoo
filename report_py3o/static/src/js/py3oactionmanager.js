/* Copyright 2017 ACSONE SA/NV
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define('report_py3o.report', function (require) {
    'use strict';
    var ActionManager = require('web.ActionManager');
    var crash_manager = require('web.crash_manager');
    var framework = require('web.framework');

    var trigger_download = function(session, response, c, action, options) {
        session.get_file({
            url: '/report/download',
            data: {data: JSON.stringify(response)},
            complete: framework.unblockUI,
            error: c.rpc_error.bind(c),
            success: function(){
                if (action && options && !action.dialog) {
                    options.on_close();
                }
            },
        });
    };

    ActionManager.include({
        ir_actions_report: function(action, options) {
            var self = this;

            // Py3o reports
            if ('report_type' in action && action.report_type === 'py3o' ) {
                framework.blockUI();
                action = _.clone(action);
                var report_url = '/report/py3o/' + action.report_name;
                // generic report: no query string
                // particular: query string of action.data.form and context
                if (!('data' in action) || !(action.data)) {
                    if ('active_ids' in action.context) {
                        report_url += "/" + action.context.active_ids.join(',');
                    }
                } else {
                    report_url += "&options=" + encodeURIComponent(JSON.stringify(action.data));
                    report_url += "&context=" + encodeURIComponent(JSON.stringify(action.context));
                }

                var response = [];
                response[0] = report_url;
                response[1] = action.report_type;
                var c = crash_manager;
                return trigger_download(self.getSession(), response, c, action, options);
            }

            return self._super(action, options);
        }
    });

});
