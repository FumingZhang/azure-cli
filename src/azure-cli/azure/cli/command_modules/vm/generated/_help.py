# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['vm ssh-public-key'] = """
    type: group
    short-summary: Manage ssh public key with vm
"""

helps['vm ssh-public-key list'] = """
    type: command
    short-summary: "Lists all of the SSH public keys in the specified resource group. Use the nextLink property in the \
response to get the next page of SSH public keys. And Lists all of the SSH public keys in the subscription. Use the \
nextLink property in the response to get the next page of SSH public keys."
"""

helps['vm ssh-public-key show'] = """
    type: command
    short-summary: "Retrieves information about an SSH public key."
    examples:
      - name: Get an ssh public key.
        text: |-
               az vm ssh-public-key show --resource-group "myResourceGroup" --name "mySshPublicKeyName"
"""

helps['vm ssh-public-key create'] = """
    type: command
    short-summary: "Creates a new SSH public key resource."
    examples:
      - name: Create a new SSH public key resource.
        text: |-
               az vm ssh-public-key create --location "westus" --public-key "{ssh-rsa public key}" --resource-group \
"myResourceGroup" --name "mySshPublicKeyName"
"""

helps['vm ssh-public-key update'] = """
    type: command
    short-summary: "Updates a new SSH public key resource."
"""

helps['vm ssh-public-key delete'] = """
    type: command
    short-summary: "Delete an SSH public key."
"""

helps['vm ssh-public-key generate-key-pair'] = """
    type: command
    short-summary: "Generates and returns a public/private key pair and populates the SSH public key resource with the \
public key. The length of the key will be 3072 bits. This operation can only be performed once per SSH public key \
resource."
    examples:
      - name: Generate an SSH key pair.
        text: |-
               az vm ssh-public-key generate-key-pair --resource-group "myResourceGroup" --name "mySshPublicKeyName"
"""

helps['vm virtual-machine'] = """
    type: group
    short-summary: Manage virtual machine with vm
"""

helps['vm virtual-machine reimage'] = """
    type: command
    short-summary: "Reimages the virtual machine which has an ephemeral OS disk back to its initial state."
    examples:
      - name: Reimage a Virtual Machine.
        text: |-
               az vm virtual-machine reimage --temp-disk true --resource-group "myResourceGroup" --name "myVMName"
"""

helps['vm virtual-machine wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the vm virtual-machine is met.
    examples:
      - name: Pause executing next line of CLI script until the vm virtual-machine is successfully created.
        text: |-
               az vm ssh-public-key wait --resource-group "myResourceGroup" --name "mySshPublicKeyName" --created
"""

helps['vm virtual-machine-scale-set'] = """
    type: group
    short-summary: Manage virtual machine scale set with vm
"""

helps['vm virtual-machine-scale-set force-recovery-service-fabric-platform-update-domain-walk'] = """
    type: command
    short-summary: "Manual platform update domain walk to update virtual machines in a service fabric virtual machine \
scale set."
"""

helps['vm virtual-machine-scale-set redeploy'] = """
    type: command
    short-summary: "Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, \
and powers them back on."
"""

helps['vm virtual-machine-scale-set reimage-all'] = """
    type: command
    short-summary: "Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This \
operation is only supported for managed disks."
"""

helps['vm virtual-machine-scale-set wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the vm virtual-machine-scale-set is met.
    examples:
      - name: Pause executing next line of CLI script until the vm virtual-machine-scale-set is successfully created.
        text: |-
               az vm ssh-public-key wait --resource-group "myResourceGroup" --name "mySshPublicKeyName" --created
"""

helps['vm virtual-machine-scale-set-vm-extension'] = """
    type: group
    short-summary: Manage virtual machine scale set vm extension with vm
"""

helps['vm virtual-machine-scale-set-vm-extension list'] = """
    type: command
    short-summary: "The operation to get all extensions of an instance in Virtual Machine Scaleset."
    examples:
      - name: List extensions in Vmss instance.
        text: |-
               az vm virtual-machine-scale-set-vm-extension list --instance-id "0" --resource-group "myResourceGroup" \
--vm-scale-set-name "myvmScaleSet"
"""

helps['vm virtual-machine-scale-set-vm-extension show'] = """
    type: command
    short-summary: "The operation to get the VMSS VM extension."
    examples:
      - name: Get VirtualMachineScaleSet VM extension.
        text: |-
               az vm virtual-machine-scale-set-vm-extension show --instance-id "0" --resource-group "myResourceGroup" \
--vm-extension-name "myVMExtension" --vm-scale-set-name "myvmScaleSet"
"""

helps['vm virtual-machine-scale-set-vm-extension create'] = """
    type: command
    short-summary: "The operation to Create the VMSS VM extension."
    parameters:
      - name: --substatuses
        short-summary: "The resource status information."
        long-summary: |
            Usage: --substatuses code=XX level=XX display-status=XX message=XX time=XX

            code: The status code.
            level: The level code.
            display-status: The short localizable label for the status.
            message: The detailed status message, including for alerts and error messages.
            time: The time of the status.

            Multiple actions can be specified by using more than one --substatuses argument.
      - name: --statuses
        short-summary: "The resource status information."
        long-summary: |
            Usage: --statuses code=XX level=XX display-status=XX message=XX time=XX

            code: The status code.
            level: The level code.
            display-status: The short localizable label for the status.
            message: The detailed status message, including for alerts and error messages.
            time: The time of the status.

            Multiple actions can be specified by using more than one --statuses argument.
    examples:
      - name: Create VirtualMachineScaleSet VM extension.
        text: |-
               az vm virtual-machine-scale-set-vm-extension create --type-properties-type "extType" \
--auto-upgrade-minor-version true --publisher "extPublisher" --settings "{\\"UserName\\":\\"xyz@microsoft.com\\"}" \
--type-handler-version "1.2" --instance-id "0" --resource-group "myResourceGroup" --vm-extension-name "myVMExtension" \
--vm-scale-set-name "myvmScaleSet"
"""

helps['vm virtual-machine-scale-set-vm-extension wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the vm virtual-machine-scale-set-vm-extension \
is met.
    examples:
      - name: Pause executing next line of CLI script until the vm virtual-machine-scale-set-vm-extension is \
successfully created.
        text: |-
               az vm virtual-machine-scale-set-vm-extension wait --instance-id "0" --resource-group "myResourceGroup" \
--vm-extension-name "myVMExtension" --vm-scale-set-name "myvmScaleSet" --created
"""

helps['vm virtual-machine-scale-set-v-ms'] = """
    type: group
    short-summary: Manage virtual machine scale set v ms with vm
"""

helps['vm virtual-machine-scale-set-v-ms redeploy'] = """
    type: command
    short-summary: "Shuts down the virtual machine in the virtual machine scale set, moves it to a new node, and \
powers it back on."
"""

helps['vm virtual-machine-scale-set-v-ms reimage-all'] = """
    type: command
    short-summary: "Allows you to re-image all the disks ( including data disks ) in the a VM scale set instance. This \
operation is only supported for managed disks."
"""

helps['vm virtual-machine-scale-set-v-ms retrieve-boot-diagnostic-data'] = """
    type: command
    short-summary: "The operation to retrieve SAS URIs of boot diagnostic logs for a virtual machine in a VM scale \
set."
    examples:
      - name: RetrieveBootDiagnosticsData of a virtual machine.
        text: |-
               az vm virtual-machine-scale-set-v-ms retrieve-boot-diagnostic-data --instance-id "0" --resource-group \
"ResourceGroup" --sas-uri-expiration-time-in-minutes 60 --vm-scale-set-name "myvmScaleSet"
"""

helps['vm virtual-machine-scale-set-v-ms wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the vm virtual-machine-scale-set-v-ms is met.
    examples:
      - name: Pause executing next line of CLI script until the vm virtual-machine-scale-set-v-ms is successfully \
created.
        text: |-
               az vm virtual-machine-scale-set-vm-extension wait --instance-id "0" --resource-group "myResourceGroup" \
--vm-extension-name "myVMExtension" --vm-scale-set-name "myvmScaleSet" --created
"""

helps['vm virtual-machine-scale-set-vm-run-command'] = """
    type: group
    short-summary: Manage virtual machine scale set vm run command with vm
"""

helps['vm virtual-machine-scale-set-vm-run-command list'] = """
    type: command
    short-summary: "The operation to get all run commands of an instance in Virtual Machine Scaleset."
    examples:
      - name: List run commands in Vmss instance.
        text: |-
               az vm virtual-machine-scale-set-vm-run-command list --instance-id "0" --resource-group \
"myResourceGroup" --vm-scale-set-name "myvmScaleSet"
"""

helps['vm disk-access'] = """
    type: group
    short-summary: Manage disk access with vm
"""

helps['vm disk-access delete-a-private-endpoint-connection'] = """
    type: command
    short-summary: "Deletes a private endpoint connection under a disk access resource."
    examples:
      - name: Delete a private endpoint connection under a disk access resource.
        text: |-
               az vm disk-access delete-a-private-endpoint-connection --name "myDiskAccess" \
--private-endpoint-connection-name "myPrivateEndpointConnection" --resource-group "myResourceGroup"
"""

helps['vm disk-access show-private-link-resource'] = """
    type: command
    short-summary: "Gets the private link resources possible under disk access resource."
    examples:
      - name: List all possible private link resources under disk access resource.
        text: |-
               az vm disk-access show-private-link-resource --name "myDiskAccess" --resource-group "myResourceGroup"
"""

helps['vm disk-access wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the vm disk-access is met.
    examples:
      - name: Pause executing next line of CLI script until the vm disk-access is successfully created.
        text: |-
               az vm virtual-machine-scale-set-vm-extension wait --instance-id "0" --resource-group "myResourceGroup" \
--vm-extension-name "myVMExtension" --vm-scale-set-name "myvmScaleSet" --created
"""

helps['vm gallery-application'] = """
    type: group
    short-summary: Manage gallery application with vm
"""

helps['vm gallery-application list'] = """
    type: command
    short-summary: "List gallery Application Definitions in a gallery."
    examples:
      - name: List gallery Applications in a gallery.
        text: |-
               az vm gallery-application list --gallery-name "myGalleryName" --resource-group "myResourceGroup"
"""

helps['vm gallery-application show'] = """
    type: command
    short-summary: "Retrieves information about a gallery Application Definition."
    examples:
      - name: Get a gallery Application.
        text: |-
               az vm gallery-application show --name "myGalleryApplicationName" --gallery-name "myGalleryName" \
--resource-group "myResourceGroup"
"""

helps['vm gallery-application create'] = """
    type: command
    short-summary: "Create a gallery Application Definition."
    examples:
      - name: Create or update a simple gallery Application.
        text: |-
               az vm gallery-application create --location "West US" --description "This is the gallery application \
description." --eula "This is the gallery application EULA." --privacy-statement-uri "myPrivacyStatementUri}" \
--release-note-uri "myReleaseNoteUri" --supported-os-type "Windows" --name "myGalleryApplicationName" --gallery-name \
"myGalleryName" --resource-group "myResourceGroup"
"""

helps['vm gallery-application delete'] = """
    type: command
    short-summary: "Delete a gallery Application."
    examples:
      - name: Delete a gallery Application.
        text: |-
               az vm gallery-application delete --name "myGalleryApplicationName" --gallery-name "myGalleryName" \
--resource-group "myResourceGroup"
"""

helps['vm gallery-application wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the vm gallery-application is met.
    examples:
      - name: Pause executing next line of CLI script until the vm gallery-application is successfully created.
        text: |-
               az vm gallery-application wait --name "myGalleryApplicationName" --gallery-name "myGalleryName" \
--resource-group "myResourceGroup" --created
      - name: Pause executing next line of CLI script until the vm gallery-application is successfully deleted.
        text: |-
               az vm gallery-application wait --name "myGalleryApplicationName" --gallery-name "myGalleryName" \
--resource-group "myResourceGroup" --deleted
"""

helps['vm gallery-application-version'] = """
    type: group
    short-summary: Manage gallery application version with vm
"""

helps['vm gallery-application-version list'] = """
    type: command
    short-summary: "List gallery Application Versions in a gallery Application Definition."
    examples:
      - name: List gallery Application Versions in a gallery Application Definition.
        text: |-
               az vm gallery-application-version list --gallery-application-name "myGalleryApplicationName" \
--gallery-name "myGalleryName" --resource-group "myResourceGroup"
"""
