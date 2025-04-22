from .config import RamalamaImplConfig


async def get_adapter_impl(config: RamalamaImplConfig, _deps):
    from .ramalama import RamalamaInferenceAdapter

    impl = RamalamaInferenceAdapter(config.url)
    await impl.initialize()
    return impl
