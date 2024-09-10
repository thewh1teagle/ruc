pushd ruc/target/release
cargo build --release
mkdir -p ruc
cp libruc.a libruc.dylib ruc/
cp ../../ruc.h ruc/
tar -czf ruc.tar.gz ruc
