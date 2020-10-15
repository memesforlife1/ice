Name:Ice
Version: 6.0.8
Release: 6.0.8
Summary: Tool to create Chromium/Chrome/Firefox/Vivaldi SSBs in Peppermint OS Ported to fedora.

License: GPLv2
Source0: 
BuildArch: x86_64

%description
Application to easily add and remove Chromium site specific browsers in Debian and Ubuntu based Linux distributions. It was originally created for Peppermint OS Ice and is now used as the default SSB application in Peppermint OS since the two branches of the OS merged for Peppermint Two. Since version 5, Ice has supported Google Chrome. Ice now supports Chrome, Chromium, Firefox, and Vivaldi. Chrome, Chromium, and Vivaldi SSB's can now be completely isolated from each other (or use the shared master browser profile) Firefox SSB's are always isolated.
%install

%files
%{_bindir}/ice
%changelog


