git lfs track '*.png'
git lfs migrate import --include="*.png" --everything

install gitlab-runner

concurrent = 1
check_interval = 0
connection_max_age = "15m0s"
shutdown_timeout = 0

[session_server]
  session_timeout = 1800

[[runners]]
  name = "DESKTOP-NHH6V43"
  url = "https://gitlab.com"
  id = 38448242
  token = "*****"
  token_obtained_at = 2024-06-12T19:25:12Z
  token_expires_at = 0001-01-01T00:00:00Z
  executor = "docker"
  [runners.custom_build_dir]
  [runners.cache]
    MaxUploadedArchiveSize = 0
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "ruby:2.7"
    privileged = true #set TRUE
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
    network_mtu = 0
