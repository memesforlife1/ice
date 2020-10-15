Name:    Ice Web App Manager
Version: 6.0.8
Release: 1%{?dist}
Summary: Tool to create Chromium/Chrome/Firefox/Vivaldi SSBs in Peppermint OS Ported to fedora.

License: Public Domain
Source0: howdy

%description
Application to easily add and remove Chromium site specific browsers in Debian and Ubuntu based Linux distributions. It was originally created for Peppermint OS Ice and is now used as the default SSB application in Peppermint OS since the two branches of the OS merged for Peppermint Two. Since version 5, Ice has supported Google Chrome. Ice now supports Chrome, Chromium, Firefox, and Vivaldi. Chrome, Chromium, and Vivaldi SSB's can now be completely isolated from each other (or use the shared master browser profile) Firefox SSB's are always isolated.
%install
fpm -s dir -t rpm -n ice usr
%files
%{_bindir}/ice
%changelog


