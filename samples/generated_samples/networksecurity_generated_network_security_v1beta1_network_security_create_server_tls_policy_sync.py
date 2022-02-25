# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateServerTlsPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-network-security


# [START networksecurity_generated_network_security_v1beta1_NetworkSecurity_CreateServerTlsPolicy_sync]
from google.cloud import network_security_v1beta1


def sample_create_server_tls_policy():
    # Create a client
    client = network_security_v1beta1.NetworkSecurityClient()

    # Initialize request argument(s)
    server_tls_policy = network_security_v1beta1.ServerTlsPolicy()
    server_tls_policy.name = "name_value"

    request = network_security_v1beta1.CreateServerTlsPolicyRequest(
        parent="parent_value",
        server_tls_policy_id="server_tls_policy_id_value",
        server_tls_policy=server_tls_policy,
    )

    # Make the request
    operation = client.create_server_tls_policy(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END networksecurity_generated_network_security_v1beta1_NetworkSecurity_CreateServerTlsPolicy_sync]