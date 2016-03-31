# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2016, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DeleteView

from shoop.core.models import ContactGroup


class ContactGroupDeleteView(DeleteView):
    model = ContactGroup
    success_url = reverse_lazy("shoop_admin:contact-group.list")