Summary:	Utilities for managing the XFS filesystem
Name:		xfsprogs
Version:	5.0.0
Release:	12%{?dist}
License:	GPL+ and LGPLv2+
Group:		System Environment/Base
URL:		https://xfs.wiki.kernel.org
Source0:	http://kernel.org/pub/linux/utils/fs/xfs/xfsprogs/%{name}-%{version}.tar.xz
BuildRequires:	gcc
BuildRequires:	libtool, gettext, libattr-devel, libuuid-devel
BuildRequires:	readline-devel, libblkid-devel >= 2.17-0.1.git5e51568
BuildRequires:	lvm2-devel, libicu-devel >= 4.6
Provides:	xfs-cmds
Obsoletes:	xfs-cmds <= %{version}
Provides:	xfsprogs-qa-devel
Obsoletes:	xfsprogs-qa-devel <= %{version}
Conflicts:	xfsdump < 3.0.1

# reflink is not yet default upstream, but we enabled it as such
Patch0:		xfsprogs-4.17.0-reflink-default.patch
Patch1:		xfsprogs-5.1.0-mkfs-validate-start-and-end-of-aligned-logs.patch
Patch2:		xfsprogs-5.1.0-mkfs-don-t-use-xfs_verify_fsbno-before-m_sb-is-fully.patch
Patch3:		xfsprogs-5.1.0-xfsprogs-Fix-uninitialized-cfg-lsunit.patch
Patch4:		xfsprogs-5.3.0-xfs_growfs-allow-mounted-device-node-as-argument.patch
Patch5:		xfsprogs-5.5.0-libxfs-use-FALLOC_FL_ZERO_RANGE-in-libxfs_device_zer.patch
Patch6:		xfsprogs-5.4.0-mkfs-Break-block-discard-into-chunks-of-2-GB.patch
Patch7:		xfsprogs-5.4.0-mkfs-tidy-up-discard-notifications.patch
Patch8:		xfsprogs-5.7.0-xfs_quota-refactor-code-to-generate-id-from-name.patch
Patch9:		xfsprogs-5.7.0-xfs_quota-allow-individual-timer-extension.patch
Patch10:	xfsprogs-5.7.0-xfs_quota-fix-unsigned-int-id-comparisons.patch
Patch11:	xfsprogs-5.7.0-xfs_repair-check-for-AG-btree-records-that-would-wra.patch
Patch12:	xfsprogs-5.7.0-xfs_repair-tag-inobt-vs-finobt-errors-properly.patch
Patch13:	xfsprogs-5.7.0-xfs_repair-complain-about-bad-interior-btree-pointer.patch
Patch14:	xfsprogs-5.7.0-xfs_repair-convert-to-libxfs_verify_agbno.patch
Patch15:	xfsprogs-5.9.0-mkfs.xfs-fix-ASSERT-on-too-small-device-with-stripe.patch
Patch16:	xfsprogs-5.7.0-xfs_repair-fix-rebuilding-btree-block-less-than-minr.patch
Patch17:	xfsprogs-5.10.0-xfs_quota-document-how-the-default-quota-is-stored.patch
Patch18:	xfsprogs-5.8.0-xfs_db-short-circuit-type_f-if-type-is-unchanged.patch
Patch19:	xfsprogs-5.10.0-xfs_repair-Use-proper-min-max-values-in-compute_level_geometry.patch
Patch20:	xfsprogs-5.8.0-xfs_quota-command-error-message-improvement.patch
Patch21:	xfsprogs-5.8.0-xfs_quota-display-warning-limits-when-printing-quota.patch
Patch22:	xfsprogs-5.8.0-xfs_quota-state-command-should-report-ugp-grace-time.patch
Patch23:	xfsprogs-5.1.0-libxfs-create-current_time-helper-and-sync-xfs_trans.patch
Patch24:	xfsprogs-5.5.0-xfs-use-a-struct-timespec64-for-the-in-core-crtime.patch
Patch25:	xfsprogs-5.9.0-xfs-drop-the-type-parameter-from-xfs_dquot_verify.patch
Patch26:	xfsprogs-5.9.0-xfs-improve-ondisk-dquot-flags-checking.patch
Patch27:	xfsprogs-5.10.0-libxfs-create-a-real-struct-timespec64.patch
Patch28:	xfsprogs-5.10.0-libxfs-refactor-NSEC_PER_SEC.patch
Patch29:	xfsprogs-5.10.0-xfs-store-inode-btree-block-counts-in-AGI-header.patch
Patch30:	xfsprogs-5.10.0-xfs-use-the-finobt-block-counts-to-speed-up-mount-ti.patch
Patch31:	xfsprogs-5.10.0-xfs-explicitly-define-inode-timestamp-range.patch
Patch32:	xfsprogs-5.10.0-xfs-refactor-quota-expiration-timer-modification.patch
Patch33:	xfsprogs-5.10.0-xfs-refactor-default-quota-grace-period-setting-code.patch
Patch34:	xfsprogs-5.10.0-xfs-refactor-quota-timestamp-coding.patch
Patch35:	xfsprogs-5.10.0-xfs-move-xfs_log_dinode_to_disk-to-the-log-recovery-.patch
Patch36:	xfsprogs-5.10.0-xfs-redefine-xfs_timestamp_t.patch
Patch37:	xfsprogs-5.10.0-xfs-redefine-xfs_ictimestamp_t.patch
Patch38:	xfsprogs-5.10.0-xfs-widen-ondisk-inode-timestamps-to-deal-with-y2038.patch
Patch39:	xfsprogs-5.10.0-xfs-widen-ondisk-quota-expiration-timestamps-to-hand.patch
Patch40:	xfsprogs-5.10.0-xfs_db-support-displaying-inode-btree-block-counts-i.patch
Patch41:	xfsprogs-5.10.0-xfs_repair-check-inode-btree-block-counters-in-AGI.patch
Patch42:	xfsprogs-5.10.0-xfs_repair-regenerate-inode-btree-block-counters-in-.patch
Patch43:	xfsprogs-5.10.0-xfs-enable-new-inode-btree-counters-feature.patch
Patch44:	xfsprogs-5.10.0-mkfs-enable-the-inode-btree-counter-feature.patch
Patch45:	xfsprogs-5.10.0-libfrog-convert-cvttime-to-return-time64_t.patch
Patch46:	xfsprogs-5.10.0-xfs_quota-convert-time_to_string-to-use-time64_t.patch
Patch47:	xfsprogs-5.10.0-xfs_db-refactor-timestamp-printing.patch
Patch48:	xfsprogs-5.10.0-xfs_db-refactor-quota-timer-printing.patch
Patch49:	xfsprogs-5.10.0-libfrog-list-the-bigtime-feature-when-reporting-geom.patch
Patch50:	xfsprogs-5.10.0-xfs_db-report-bigtime-format-timestamps.patch
Patch51:	xfsprogs-5.10.0-xfs_db-support-printing-time-limits.patch
Patch52:	xfsprogs-5.10.0-xfs_quota-support-editing-and-reporting-quotas-with-.patch
Patch53:	xfsprogs-5.10.0-xfs_repair-support-bigtime-timestamp-checking.patch
Patch54:	xfsprogs-5.10.0-xfs-enable-big-timestamps.patch
Patch55:	xfsprogs-5.10.0-mkfs-format-bigtime-filesystems.patch
Patch56:	xfsprogs-5.12.0-libxfs-copy-crtime-correctly-now-that-it-s-timespec6.patch
Patch57:	xfsprogs-5.13.0-xfs-remove-the-unused-xfs_icdinode_has_bigtime-helpe.patch
Patch58:	xfsprogs-5.13.0-xfs-rename-xfs_ictimestamp_t.patch
Patch59:	xfsprogs-5.13.0-xfs-rename-struct-xfs_legacy_ictimestamp.patch
Patch60:	xfsprogs-5.11.0-mkfs-fix-wrong-inobtcount-usage-error-output.patch
Patch61:	xfsprogs-5.12.0-libxfs-expose-inobtcount-in-xfs-geometry.patch
Patch62:	xfsprogs-5.12.0-libfrog-report-inobtcount-in-geometry.patch
Patch63:	xfsprogs-5.19.0-xfs_repair-ignore-empty-xattr-leaf-blocks.patch
Patch64:	xfsprogs-5.19.0-mkfs-terminate-getsubopt-arrays-properly.patch
Patch65:	xfsprogs-5.9.0-xfs-ignore-autofs-mount-table-entries.patch
Patch66:	xfsprogs-5.10.0-xfs_repair-fix-progress-reporting.patch
Patch67:	xfsprogs-rhelonly-mkfs-fix-man-s-default-value-for-sparse-option.patch

%description
A set of commands to use the XFS filesystem, including mkfs.xfs.

XFS is a high performance journaling filesystem which originated
on the SGI IRIX platform.  It is completely multi-threaded, can
support large files and large filesystems, extended attributes,
variable block sizes, is extent based, and makes extensive use of
Btrees (directories, extents, free space) to aid both performance
and scalability.

This implementation is on-disk compatible with the IRIX version
of XFS.

%package devel
Summary: XFS filesystem-specific headers
Group: Development/Libraries
Requires: xfsprogs = %{version}-%{release}, libuuid-devel

%description devel
xfsprogs-devel contains the header files needed to develop XFS
filesystem-specific programs.

You should install xfsprogs-devel if you want to develop XFS
filesystem-specific programs,  If you install xfsprogs-devel, you'll
also want to install xfsprogs.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1

%build
export tagname=CC

%configure \
        --enable-readline=yes	\
	--enable-blkid=yes	\
	--enable-lto=no		\
	--enable-scrub=no

# NOTE scrub manpages manually removed below as well

make V=1 %{?_smp_mflags}

%install
make DIST_ROOT=$RPM_BUILD_ROOT install install-dev \
	PKG_ROOT_SBIN_DIR=%{_sbindir} PKG_ROOT_LIB_DIR=%{_libdir}

# nuke .la files, etc
rm -f $RPM_BUILD_ROOT/{%{_lib}/*.{la,a,so},%{_libdir}/*.{la,a}}

# remove non-versioned docs location
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/xfsprogs/

# Remove scrub manpages
rm -rf $RPM_BUILD_ROOT/%{_mandir}/man8/xfs_scrub*

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc doc/CHANGES README
%{_libdir}/*.so.*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sbindir}/*

%files devel
%{_mandir}/man2/*
%{_mandir}/man3/*
%dir %{_includedir}/xfs
%{_includedir}/xfs/handle.h
%{_includedir}/xfs/jdm.h
%{_includedir}/xfs/linux.h
%{_includedir}/xfs/xfs.h
%{_includedir}/xfs/xfs_arch.h
%{_includedir}/xfs/xfs_fs.h
%{_includedir}/xfs/xfs_types.h
%{_includedir}/xfs/xfs_format.h
%{_includedir}/xfs/xfs_da_format.h
%{_includedir}/xfs/xfs_log_format.h
%{_includedir}/xfs/xqm.h

%{_libdir}/*.so

%changelog
* Thu Jun 08 2023 Pavel Reichl <preichl@redhat.com> - 5.0.0-12
- Fix xfs_repair progress reporting is not working (#2183398)
- Fix man page default for sparse mkfs option (#2118564)

* Tue May 02 2023 Pavel Reichl <preichl@redhat.com> - 5.0.0-11
- Fix xfstest fails with error "missing xfsprogs fix patch"(#2161936,#2160746)
- Fix ignore autofs mount table entries (#2182361)

* Thu Dec 09 2021 Bill O'Donnell <bodonnel@redhat.com> 5.0.0-10
- xfsprogs: enable bigtime and inode btree counter features in RHEL8 (#2024201))

* Thu Jul 08 2021 Bill O'Donnell <bodonnel@redhat.com> 5.0.0-9
- xfs_quota: state command should report ugp grace time (#1949743)

* Thu Jan 07 2021 Bill O'Donnell <billodo@redhat.com> 5.0.0-8
- xfs_repair: Use proper min/max values in compute_level_geometry (#1910384)

* Mon Dec 14 2020 Bill O'Donnell <billodo@redhat.com> 5.0.0-7
- xfs_quota: document how the default quota is stored (#1850188)
- xfs_db: skip type change if type_f unchanged (#1867474)

* Wed Dec 09 2020 Bill O'Donnell <billodo@redhat.com> 5.0.0-6
- xfs_repair: improve AG btree ptr validation (libxfs_verify_agbno) (#1887288)
- mkfs.xfs: fix ASSERT on too-small device with stripe geometry (#1887401)
- xfs_repair: fix rebuilding btree block less than minrecs (#1759452)

* Wed Dec 02 2020 Bill O'Donnell <billodo@redhat.com> 5.0.0-5
- xfs_quota: allow individual timer extension (#1899204)

* Wed Jun 03 2020 Eric Sandeen <sandeen@redhat.com> 5.0.0-4
- mkfs.xfs: inform user about discard, and make interruptable (#1836414)

* Mon Apr 20 2020 Eric Sandeen <sandeen@redhat.com> 5.0.0-3
- mkfs.xfs: use faster log zeroing on supported devices (#1755046)

* Sat Dec 14 2019 Eric Sandeen <sandeen@redhat.com> 5.0.0-2
- mkfs.xfs: validate log stripe unit alignment (#1632596)
- xfs_growfs: allow mounted device node as argument (#1765217)

* Tue May 21 2019 Eric Sandeen <sandeen@redhat.com> 5.0.0-1
- New upstream version (#1712147)
- mkfs.xfs: validate extent size hint parameters (#1683007)
- mkfs.xfs: null-terminate symlinks created via protofile (#1640503)
- xfs_repair: allow '/' in attribute names (#1667354)
- xfs_info: allow device name as parameter (#1679840)
- xfs_quota: fix project inheritance flag handling (#1664105)
- xfs_metadump: handle symlinks correctly (#1693074)
- xfs_db: fix finobt record decoding with sparse inodes (#1690245)

* Mon Feb 04 2019 Eric Sandeen <sandeen@redhat.com> 4.19.0-2
- xfs_repair: initialize non-leaf finobt blocks with correct magic (#1670153)

* Tue Nov 27 2018 Eric Sandeen <sandeen@redhat.com> 4.19.0-1
- New upstream release (#1652248)
- Note reflink default in mkfs.xfs manpage (#1641698)
- Fix xfs_db sign extension in agi freecount (#1640090)
- Fix xfs_repair hang on large filesystem (#1630674)

* Tue Sep 25 2018 Eric Sandeen <sandeen@redhat.com> 4.18.0-3
- Remove experimental xfs_scrub utility (#1623301)

* Wed Sep 19 2018 Eric Sandeen <sandeen@redhat.com> 4.18.0-2
- Fix annobin checks (#1630641)

* Tue Aug 28 2018 Eric Sandeen <sandeen@redhat.com> 4.18.0-1
- New upstream release (#1623695)

* Mon Aug 13 2018 Eric Sandeen <sandeen@redhat.com> 4.17.0-4
- Disable reflink automatically if crcs are disabled (#1600610)

* Wed Aug 01 2018 Charalampos Stratakis <cstratak@redhat.com> - 4.17.0-3
- Rebuild for platform-python

* Thu Jun 28 2018 Eric Sandeen <sandeen@redhat.com> 4.17.0-2
- Default mkfs to reflink enabled (#1494028)

* Thu Jun 28 2018 Eric Sandeen <sandeen@redhat.com> 4.17.0-1
- New upstream release
- Clean up spec file

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> 4.15.1-1
- New upstream release
- Update Polish translation

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> 4.15.0-2
- BuildRequires: gcc

* Sat Feb 24 2018 Eric Sandeen <sandeen@redhat.com> 4.15.0-1
- New upstream release
- Adds new xfs_scrub utility and services

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Eric Sandeen <sandeen@redhat.com> 4.14.0-1
- New upstream release

* Wed Sep 27 2017 Eric Sandeen <sandeen@redhat.com> 4.13.1-1
- New upstream release
- Trim ancient changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 4.12.0-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Eric Sandeen <sandeen@redhat.com> 4.12.0-1
- New upstream release

* Fri May 05 2017 Eric Sandeen <sandeen@redhat.com> 4.11.0-1
- New upstream release

* Sun Feb 26 2017 Eric Sandeen <sandeen@redhat.com> 4.10.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.9.0-2
- Rebuild for readline 7.x

* Thu Jan 05 2017 Eric Sandeen <sandeen@redhat.com> 4.9.0-1
- New upstream release

* Tue Oct 18 2016 Eric Sandeen <sandeen@redhat.com> 4.8.0-1
- New upstream release

* Tue Sep 06 2016 Eric Sandeen <sandeen@redhat.com> 4.7.0-2
- Add libattr-devel build dependency to fix xfs_fsr

* Sun Sep 04 2016 Eric Sandeen <sandeen@redhat.com> 4.7.0-1
- New upstream release

* Tue Mar 15 2016 Eric Sandeen <sandeen@redhat.com> 4.5.0-1
- New upstream release

* Thu Mar 10 2016 Eric Sandeen <sandeen@redhat.com> 4.3.0-3
- Fix build w/ new kernels which have [sg]etxattr promotion

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Eric Sandeen <sandeen@redhat.com> 4.3.0-1
- New upstream release

* Wed Sep 09 2015 Eric Sandeen <sandeen@redhat.com> 4.2.0-1
- New upstream release

* Thu Jul 30 2015 Eric Sandeen <sandeen@redhat.com> 3.2.4-1
- New upstream release
- Addresses CVE-2012-2150 for xfs_metadump

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Eric Sandeen <sandeen@redhat.com> 3.2.3-1
- New upstream release
