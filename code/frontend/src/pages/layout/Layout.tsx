import { Outlet, Link } from "react-router-dom";
import styles from "./Layout.module.css";
import Azure from "../../../public/buma.png";
import { CopyRegular, ShareRegular } from "@fluentui/react-icons";
import { Dialog, Stack, TextField } from "@fluentui/react";
import { useEffect, useState } from "react";

const Layout = () => {
    const handleUploadClick = () => {
        window.location.href = 'http://localhost/bumadb/login.php';
    };

    return (
        <div className={styles.layout}>
            <header className={styles.header} role={"banner"}>
                <div className={styles.headerContainer}>
                    <Stack horizontal verticalAlign="center">
                        <img
                            src={Azure}
                            className={styles.headerIcon}
                            aria-hidden="true"
                            alt="BUMA AI logo"
                        />
                        <Link to="/" className={styles.headerTitleContainer}>
                            <h3 className={styles.headerTitle}>BUMA AI</h3>
                        </Link>
                        <div
                            className={styles.shareButtonContainer}
                            role="button"
                            tabIndex={0}
                            aria-label="Upload"
                            onClick={handleUploadClick}
                            onKeyDown={(e) =>
                                e.key === "Enter" || e.key === " " ? handleUploadClick() : null
                            }
                            style={{ cursor: 'pointer' }}
                        >
                            <span className={styles.shareButtonText}>Panel</span>
                        </div>
                    </Stack>
                </div>
            </header>
            <Outlet />
        </div>
    );
};

export default Layout;
