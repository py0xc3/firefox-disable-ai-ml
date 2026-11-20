# firefox-disable-ai-ml
Disable AI/ML features in FF, and keep "disabled feature" list updated against current FF versions

# Environment
This is intended to be packaged as `rpm` for Fedora or its interwoven downstream distributions (CentOS Stream, AlmaLinux, RockyLinux through EPEL) and used in conjunction with these distributions' default Firefox build. It is assumed this package is kept updated through an update repository that is aligned with the distribution's default Firefox build (default repo or epel). Support also includes the Firefox of Silverblue/Kinoite base images, but not yet any Firefox flatpak.

**Only Fedora is available at this time: EPEL to follow later after more testing with CentOS/AlmaLinux/RockyLinux.**

# Description 
By default, Firefox enables certain AI/ML preferences. The "Block AI" option in the settings does not disable them but only hides them. This means, users must disable these preferences manually in about:config and thus know what they are doing: there are many AI/ML preferences that could change over time, while existing documentation does not determine any preference that disables all AI/ML reliably throughout future versions: this forces users to monitor
their settings themselves if they do not want AI/ML enabled. This package will disable AI/ML preferences automatically and if Firefox changes its AI/ML preferences in future, the package can auto-update the preferences to keep AI/ML disabled for users who want it that way.

**Note:**

When the "Block AI" option of Firefox is updated to disable AI features (patched in Fedora's build or upstream), this package is intended to be obsoleted but it is aimed to set the "Block AI" option to disabled during the package's removal (if the removal takes place through obsoleting during an update) in order to retain the known user preference (disabled AI/ML) that the user expects. 

Changes about this will be aligned with downstream (CentOS Stream, Alma, Rocky). Separate versions for Fedora's repo and EPEL will be maintained if necessary.

## Community-effort to keep the preferences of this package up to date against Firefox versions

This package is intended to be a community effort, in which every Firefox user who knows of `about:config` can contribute: if any one user finds changed or new AI/ML settings that enable any AI/ML despite the installed package, they can report it against the [source repo](https://github.com/py0xc3/ff-disable-ai-ml/issues) so that all users can get an update that keeps AI/ML disabled through the package. 

# Implementation

This package uses Mozilla's [AutoConfig](https://support.mozilla.org/en-US/kb/customizing-firefox-using-autoconfig) to implement the disabling. Using `policies.json` is intentionally avoided to not accidentally delete/override user, admin or enterprise/organization policies and customizations: `policies.json` is not intended to be be owned by a separate package.

Disabling the AI features in Firefox by default will not be possible and this package is intended to be installed manually by the user/admin.

# Versions, migrated repo

This source repo was migrated from [ff-disable-ai-ml](https://github.com/py0xc3/ff-disable-ai-ml): versions 0.1 to 0.3 are in the original repo. This one begins with 0.4.
