{pkgs}: {
  deps = [
    pkgs.openssh
    pkgs.mpi
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
    pkgs.postgresql
  ];
}
