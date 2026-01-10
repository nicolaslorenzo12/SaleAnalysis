from __future__ import annotations

from dataclasses import asdict

from sqlalchemy import Engine, text


def load_rows(
    dw_engine: Engine,
    table_name: str,
    insert_sql: str,
    rows: list[object],
    truncate: bool = True,
    batch_size: int | None = None,
) -> None:
    stmt = text(insert_sql)

    with dw_engine.begin() as conn:
        if truncate:
            conn.execute(text(f"TRUNCATE TABLE {table_name};"))

        if batch_size:
            for i in range(0, len(rows), batch_size):
                batch = [asdict(r) for r in rows[i : i + batch_size]]
                if batch:
                    conn.execute(stmt, batch)
        else:
            conn.execute(stmt, [asdict(r) for r in rows])
