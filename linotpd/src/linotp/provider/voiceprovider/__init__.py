# -*- coding: utf-8 -*-
#
#    LinOTP - the open source solution for two factor authentication
#    Copyright (C) 2010 - 2017 KeyIdentity GmbH
#
#    This file is part of LinOTP server.
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU Affero General Public
#    License, version 3, as published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the
#               GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#    E-mail: linotp@keyidentity.com
#    Contact: www.linotp.org
#    Support: www.keyidentity.com
#
'''
'''


class TwillioMixin():

    @staticmethod
    def load_twilio_definition(configDict):
        """
        load the twilio voice service configuration
        """

        if "twilio" not in configDict:
            return {}

        twilio_config = configDict["twilio"]
        if "accountSid" not in twilio_config:
            raise KeyError('missing the required account identifier')

        if "authToken" not in twilio_config:
            raise KeyError('missing the required authentication token')

        if "voice" not in twilio_config:
            twilio_config['voice'] = 'alice'

        return twilio_config
