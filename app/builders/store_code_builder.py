class StoreCodeBuilder:
    """
    Store code helper.

    Responsible for translating store code
    into transfer filename components.
    """

    PREFIX = {

        "T": "HR",

        "F": "FR",

        "R": "CR"

    }

    @classmethod
    def transfer_prefix(
        cls,
        store: str
    ) -> str:

        if not store:

            raise ValueError(
                "Store code is empty."
            )

        key = store[0].upper()

        prefix = cls.PREFIX.get(key)

        if prefix is None:

            raise ValueError(
                f"Unknown store type : {store}"
            )

        return prefix

    @staticmethod
    def transfer_suffix(
        store: str
    ) -> str:

        if len(store) < 4:

            raise ValueError(
                "Invalid store code."
            )

        return store[-3:].upper()