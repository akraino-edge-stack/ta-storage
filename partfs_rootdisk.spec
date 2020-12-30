# Copyright 2019 Nokia
  
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

%define RPM_MINOR_VERSION 3

Name:       partfs_rootdisk
Version:    %{_version}
Release:    %{RPM_MINOR_VERSION}%{?dist}
Summary:    partfs_rootdisk
License:    %{_platform_license}
Source0:    %{name}-%{version}.tar.gz
Vendor:     %{_platform_vendor}
BuildArch:  noarch

%description
Configure root disk partitions

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/etc/opt/localstorage
rsync -av partfs_rootdisk/localstorage/* %{buildroot}/etc/opt/localstorage

%files
/etc/opt/localstorage

%post
