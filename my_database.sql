--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-1.pgdg16.04+1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-1.pgdg18.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: administracao_acao; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.administracao_acao (
    id integer NOT NULL,
    nome character varying(200) NOT NULL,
    campanha_id integer NOT NULL
);


ALTER TABLE public.administracao_acao OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_acao_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.administracao_acao_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administracao_acao_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_acao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.administracao_acao_id_seq OWNED BY public.administracao_acao.id;


--
-- Name: administracao_aluno; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.administracao_aluno (
    id integer NOT NULL,
    sexo character varying(2),
    nascimento date,
    periodo character varying(2),
    turma character varying(200),
    escola_id integer NOT NULL,
    raca character varying(2),
    numero_identificacao character varying(200) NOT NULL
);


ALTER TABLE public.administracao_aluno OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_aluno_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.administracao_aluno_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administracao_aluno_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_aluno_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.administracao_aluno_id_seq OWNED BY public.administracao_aluno.id;


--
-- Name: administracao_campanha; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.administracao_campanha (
    id integer NOT NULL,
    nome character varying(200) NOT NULL
);


ALTER TABLE public.administracao_campanha OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_campanha_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.administracao_campanha_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administracao_campanha_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_campanha_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.administracao_campanha_id_seq OWNED BY public.administracao_campanha.id;


--
-- Name: administracao_diretor; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.administracao_diretor (
    id integer NOT NULL,
    data date,
    questao_1 character varying(2)[],
    questao_2 character varying(2),
    questao_3 character varying(2)[],
    questao_4 character varying(2),
    questao_5 character varying(2),
    questao_6 character varying(2),
    questao_7 character varying(2),
    questao_8 character varying(2),
    questao_9 character varying(2),
    questao_10 character varying(2),
    questao_11 character varying(2),
    questao_12 character varying(2),
    questao_13 character varying(2),
    questao_14 character varying(2),
    questao_15 character varying(2),
    questao_16 character varying(2),
    questao_17 character varying(2),
    questao_18 character varying(2),
    questao_19 character varying(2),
    questao_20 character varying(2),
    questao_21 character varying(2),
    questao_22 character varying(2),
    questao_23 character varying(2),
    questao_24 character varying(2),
    questao_25 character varying(2),
    questao_26 character varying(2),
    questao_27 character varying(2),
    questao_28 character varying(2)[],
    questao_29 character varying(2),
    questao_30 character varying(2),
    questao_31 character varying(2)[],
    questao_32 character varying(2),
    questao_33 character varying(2)[],
    questao_34 character varying(2),
    questao_35 character varying(2),
    questao_36 character varying(2),
    questao_37 character varying(2)[],
    questao_38 character varying(2),
    questao_39 character varying(2)[],
    questao_40 character varying(2),
    questao_41 character varying(2),
    questao_42 character varying(2),
    questao_43 character varying(2),
    questao_44 character varying(2),
    questao_45 character varying(2),
    questao_46 character varying(2),
    questao_47 character varying(2),
    questao_48 character varying(2),
    questao_49 character varying(2),
    questao_50 character varying(2),
    questao_51 character varying(2),
    questao_52 character varying(2),
    questao_53 character varying(2),
    questao_54 character varying(2),
    questao_55 character varying(2),
    questao_56 character varying(2),
    questao_57 character varying(2),
    questao_58 character varying(2),
    questao_59 character varying(2),
    questao_60 character varying(2),
    questao_61 character varying(2),
    questao_62 character varying(2),
    questao_63 character varying(2),
    questao_64 character varying(2),
    questao_65 character varying(2),
    questao_66 character varying(2),
    questao_67 character varying(2),
    questao_68 character varying(2),
    questao_69 character varying(2),
    questao_70 character varying(2),
    questao_71 character varying(2),
    questao_72 character varying(2),
    questao_73 character varying(2),
    questao_74 character varying(2),
    questao_75 character varying(2),
    questao_76 character varying(2),
    questao_77 character varying(2),
    questao_78 character varying(2),
    questao_79 character varying(2),
    questao_80 character varying(2),
    questao_81 character varying(2),
    questao_82 character varying(2),
    questao_83 character varying(2),
    questao_84 character varying(2),
    escola_id integer NOT NULL
);


ALTER TABLE public.administracao_diretor OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_diretor_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.administracao_diretor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administracao_diretor_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_diretor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.administracao_diretor_id_seq OWNED BY public.administracao_diretor.id;


--
-- Name: administracao_escola; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.administracao_escola (
    id integer NOT NULL,
    nome character varying(200) NOT NULL,
    acao_id integer NOT NULL,
    latitude numeric(22,18) NOT NULL,
    longitude numeric(22,18) NOT NULL
);


ALTER TABLE public.administracao_escola OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_escola_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.administracao_escola_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administracao_escola_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_escola_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.administracao_escola_id_seq OWNED BY public.administracao_escola.id;


--
-- Name: administracao_exame; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.administracao_exame (
    id integer NOT NULL,
    data date,
    examinador character varying(200),
    anotador character varying(200),
    aluno_id integer NOT NULL,
    carie_coroa_11 character varying(2),
    carie_coroa_12 character varying(2),
    carie_coroa_13 character varying(2),
    carie_coroa_14 character varying(2),
    carie_coroa_15 character varying(2),
    carie_coroa_16 character varying(2),
    carie_coroa_17 character varying(2),
    carie_coroa_18 character varying(2),
    carie_coroa_21 character varying(2),
    carie_coroa_22 character varying(2),
    carie_coroa_23 character varying(2),
    carie_coroa_24 character varying(2),
    carie_coroa_25 character varying(2),
    carie_coroa_26 character varying(2),
    carie_coroa_27 character varying(2),
    carie_coroa_28 character varying(2),
    carie_coroa_31 character varying(2),
    carie_coroa_32 character varying(2),
    carie_coroa_33 character varying(2),
    carie_coroa_34 character varying(2),
    carie_coroa_35 character varying(2),
    carie_coroa_36 character varying(2),
    carie_coroa_37 character varying(2),
    carie_coroa_38 character varying(2),
    carie_coroa_41 character varying(2),
    carie_coroa_42 character varying(2),
    carie_coroa_43 character varying(2),
    carie_coroa_44 character varying(2),
    carie_coroa_45 character varying(2),
    carie_coroa_46 character varying(2),
    carie_coroa_47 character varying(2),
    carie_coroa_48 character varying(2),
    carie_tratamento_11 character varying(2),
    carie_tratamento_12 character varying(2),
    carie_tratamento_13 character varying(2),
    carie_tratamento_14 character varying(2),
    carie_tratamento_15 character varying(2),
    carie_tratamento_16 character varying(2),
    carie_tratamento_17 character varying(2),
    carie_tratamento_18 character varying(2),
    carie_tratamento_21 character varying(2),
    carie_tratamento_22 character varying(2),
    carie_tratamento_23 character varying(2),
    carie_tratamento_24 character varying(2),
    carie_tratamento_25 character varying(2),
    carie_tratamento_26 character varying(2),
    carie_tratamento_27 character varying(2),
    carie_tratamento_28 character varying(2),
    carie_tratamento_31 character varying(2),
    carie_tratamento_32 character varying(2),
    carie_tratamento_33 character varying(2),
    carie_tratamento_34 character varying(2),
    carie_tratamento_35 character varying(2),
    carie_tratamento_36 character varying(2),
    carie_tratamento_37 character varying(2),
    carie_tratamento_38 character varying(2),
    carie_tratamento_41 character varying(2),
    carie_tratamento_42 character varying(2),
    carie_tratamento_43 character varying(2),
    carie_tratamento_44 character varying(2),
    carie_tratamento_45 character varying(2),
    carie_tratamento_46 character varying(2),
    carie_tratamento_47 character varying(2),
    carie_tratamento_48 character varying(2),
    periodontal_bolsa_11 character varying(2),
    periodontal_bolsa_1716 character varying(2),
    periodontal_bolsa_2627 character varying(2),
    periodontal_bolsa_31 character varying(2),
    periodontal_bolsa_3736 character varying(2),
    periodontal_bolsa_4647 character varying(2),
    periodontal_calculo_11 character varying(2),
    periodontal_calculo_1716 character varying(2),
    periodontal_calculo_2627 character varying(2),
    periodontal_calculo_31 character varying(2),
    periodontal_calculo_3736 character varying(2),
    periodontal_calculo_4647 character varying(2),
    periodontal_sangramento_11 character varying(2),
    periodontal_sangramento_1716 character varying(2),
    periodontal_sangramento_2627 character varying(2),
    periodontal_sangramento_31 character varying(2),
    periodontal_sangramento_3736 character varying(2),
    periodontal_sangramento_4647 character varying(2)
);


ALTER TABLE public.administracao_exame OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_exame_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.administracao_exame_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administracao_exame_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_exame_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.administracao_exame_id_seq OWNED BY public.administracao_exame.id;


--
-- Name: administracao_questionario; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.administracao_questionario (
    id integer NOT NULL,
    aluno_id integer NOT NULL,
    questao_1 character varying(2),
    questao_10 character varying(2),
    questao_100 character varying(2),
    questao_101 character varying(2),
    questao_102 character varying(2),
    questao_103 character varying(2),
    questao_104 character varying(2),
    questao_105 character varying(2),
    questao_106 character varying(2),
    questao_107 character varying(2),
    questao_108 character varying(2),
    questao_109 character varying(2),
    questao_11 character varying(2),
    questao_110 character varying(2),
    questao_111 character varying(2),
    questao_112 character varying(2),
    questao_113 character varying(2),
    questao_114 character varying(2),
    questao_115 character varying(2),
    questao_116 character varying(2),
    questao_117 character varying(2),
    questao_118 character varying(2),
    questao_119 character varying(2),
    questao_12 character varying(2),
    questao_120 character varying(2),
    questao_121 character varying(2),
    questao_122 character varying(2),
    questao_123 character varying(2),
    questao_124 character varying(2),
    questao_125 character varying(2),
    questao_126 character varying(2),
    questao_127 character varying(2),
    questao_128 character varying(2),
    questao_129 character varying(2),
    questao_13 character varying(2),
    questao_130 character varying(2),
    questao_131 character varying(2),
    questao_132 character varying(2),
    questao_133 character varying(2),
    questao_134 character varying(2),
    questao_135 character varying(2),
    questao_136 character varying(2),
    questao_137 character varying(2),
    questao_138 character varying(2),
    questao_139 character varying(2),
    questao_14 character varying(2),
    questao_140 character varying(2),
    questao_141 character varying(2),
    questao_142 character varying(2),
    questao_143 character varying(2),
    questao_144 character varying(2),
    questao_145 character varying(2),
    questao_146 character varying(2)[],
    questao_15 character varying(2),
    questao_16 character varying(2),
    questao_17 character varying(2),
    questao_18 character varying(2),
    questao_19 character varying(2),
    questao_2 character varying(2),
    questao_20 character varying(2),
    questao_21 character varying(2),
    questao_22 character varying(2),
    questao_23 character varying(2),
    questao_24 character varying(2),
    questao_25 character varying(2),
    questao_26 character varying(2),
    questao_27 character varying(2),
    questao_28 character varying(2),
    questao_29 character varying(2),
    questao_3 character varying(2),
    questao_30 character varying(2),
    questao_31 character varying(2),
    questao_32 character varying(2),
    questao_33 character varying(2),
    questao_34 character varying(2),
    questao_35 character varying(2),
    questao_36 character varying(2),
    questao_37 character varying(2),
    questao_38 character varying(2),
    questao_39 character varying(2),
    questao_4 character varying(2),
    questao_40 character varying(2),
    questao_41 character varying(2),
    questao_42 character varying(2),
    questao_43 character varying(2),
    questao_44 character varying(2),
    questao_45 character varying(2),
    questao_46 character varying(2),
    questao_47 character varying(2),
    questao_48 character varying(2),
    questao_49 character varying(2),
    questao_5 character varying(2),
    questao_50 character varying(2),
    questao_51 character varying(2),
    questao_52 character varying(2),
    questao_53 character varying(2),
    questao_54 character varying(2),
    questao_55 character varying(2),
    questao_56 character varying(2),
    questao_57 character varying(2),
    questao_58 character varying(2),
    questao_59 character varying(2),
    questao_6 character varying(2),
    questao_60 character varying(2)[],
    questao_61 character varying(2),
    questao_62 character varying(2),
    questao_63 character varying(2),
    questao_64 character varying(2),
    questao_65 character varying(2),
    questao_66 character varying(2),
    questao_67 character varying(2),
    questao_68 character varying(2),
    questao_7 character varying(2),
    questao_70 character varying(2),
    questao_71 character varying(2),
    questao_72 character varying(2),
    questao_73 character varying(2),
    questao_74 character varying(2),
    questao_75 character varying(2),
    questao_76 character varying(2),
    questao_77 character varying(2),
    questao_78 character varying(2),
    questao_79 character varying(2),
    questao_8 character varying(2),
    questao_80 character varying(2),
    questao_81 character varying(2),
    questao_82 character varying(2),
    questao_83 character varying(2),
    questao_84 character varying(2),
    questao_85 character varying(2),
    questao_86 character varying(2),
    questao_87 character varying(2),
    questao_88 character varying(2),
    questao_89 character varying(2),
    questao_9 character varying(2),
    questao_90 character varying(2),
    questao_91 character varying(2),
    questao_92 character varying(2),
    questao_93 character varying(2),
    questao_94 character varying(2),
    questao_95 character varying(2),
    questao_96 character varying(2),
    questao_97 character varying(2),
    questao_98 character varying(2),
    questao_99 character varying(2),
    data date,
    questao_69 character varying(2)
);


ALTER TABLE public.administracao_questionario OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_questionario_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.administracao_questionario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administracao_questionario_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: administracao_questionario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.administracao_questionario_id_seq OWNED BY public.administracao_questionario.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO pxopsbpdrfglvt;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO pxopsbpdrfglvt;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO pxopsbpdrfglvt;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO pxopsbpdrfglvt;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_documento; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.gerencia_documento (
    id integer NOT NULL,
    titulo character varying(200) NOT NULL,
    data timestamp with time zone NOT NULL,
    url character varying(200) NOT NULL
);


ALTER TABLE public.gerencia_documento OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_documento_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.gerencia_documento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gerencia_documento_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_documento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.gerencia_documento_id_seq OWNED BY public.gerencia_documento.id;


--
-- Name: gerencia_foto; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.gerencia_foto (
    id integer NOT NULL,
    titulo character varying(200) NOT NULL,
    data timestamp with time zone NOT NULL,
    url character varying(200) NOT NULL
);


ALTER TABLE public.gerencia_foto OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_foto_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.gerencia_foto_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gerencia_foto_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_foto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.gerencia_foto_id_seq OWNED BY public.gerencia_foto.id;


--
-- Name: gerencia_noticia; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.gerencia_noticia (
    id integer NOT NULL,
    titulo character varying(200) NOT NULL,
    data character varying(200) NOT NULL,
    texto text NOT NULL,
    imagem character varying(200) NOT NULL
);


ALTER TABLE public.gerencia_noticia OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_noticia_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.gerencia_noticia_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gerencia_noticia_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_noticia_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.gerencia_noticia_id_seq OWNED BY public.gerencia_noticia.id;


--
-- Name: gerencia_video; Type: TABLE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE TABLE public.gerencia_video (
    id integer NOT NULL,
    titulo character varying(200) NOT NULL,
    data timestamp with time zone NOT NULL,
    url character varying(200) NOT NULL
);


ALTER TABLE public.gerencia_video OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_video_id_seq; Type: SEQUENCE; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE SEQUENCE public.gerencia_video_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.gerencia_video_id_seq OWNER TO pxopsbpdrfglvt;

--
-- Name: gerencia_video_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER SEQUENCE public.gerencia_video_id_seq OWNED BY public.gerencia_video.id;


--
-- Name: administracao_acao id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_acao ALTER COLUMN id SET DEFAULT nextval('public.administracao_acao_id_seq'::regclass);


--
-- Name: administracao_aluno id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_aluno ALTER COLUMN id SET DEFAULT nextval('public.administracao_aluno_id_seq'::regclass);


--
-- Name: administracao_campanha id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_campanha ALTER COLUMN id SET DEFAULT nextval('public.administracao_campanha_id_seq'::regclass);


--
-- Name: administracao_diretor id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_diretor ALTER COLUMN id SET DEFAULT nextval('public.administracao_diretor_id_seq'::regclass);


--
-- Name: administracao_escola id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_escola ALTER COLUMN id SET DEFAULT nextval('public.administracao_escola_id_seq'::regclass);


--
-- Name: administracao_exame id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_exame ALTER COLUMN id SET DEFAULT nextval('public.administracao_exame_id_seq'::regclass);


--
-- Name: administracao_questionario id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_questionario ALTER COLUMN id SET DEFAULT nextval('public.administracao_questionario_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: gerencia_documento id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.gerencia_documento ALTER COLUMN id SET DEFAULT nextval('public.gerencia_documento_id_seq'::regclass);


--
-- Name: gerencia_foto id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.gerencia_foto ALTER COLUMN id SET DEFAULT nextval('public.gerencia_foto_id_seq'::regclass);


--
-- Name: gerencia_noticia id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.gerencia_noticia ALTER COLUMN id SET DEFAULT nextval('public.gerencia_noticia_id_seq'::regclass);


--
-- Name: gerencia_video id; Type: DEFAULT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.gerencia_video ALTER COLUMN id SET DEFAULT nextval('public.gerencia_video_id_seq'::regclass);


--
-- Data for Name: administracao_acao; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.administracao_acao (id, nome, campanha_id) FROM stdin;
1	Levantamento epidemiológico	1
2	Piloto	1
35	Testes	1
36	Apresentação do sistema	1
\.


--
-- Data for Name: administracao_aluno; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.administracao_aluno (id, sexo, nascimento, periodo, turma, escola_id, raca, numero_identificacao) FROM stdin;
2	1	2003-11-20	3	92.01	8	3	7064
3	1	2004-04-23	3	92.01	8	3	7172
4	1	2003-07-14	3	92.01	8	3	7257
5	3	2004-01-14	3	92.01	8	1	7307
6	1	2004-04-07	3	92.01	8	1	7154
7	1	2004-01-29	3	92.01	8	3	7197
8	1	2003-10-15	3	92.01	8	3	7481
9	3	2003-08-05	3	92.01	8	3	7497
10	0	2003-10-10	3	92.01	8	4	7137
11	0	2018-06-24	3	92.01	8	3	7229
12	0	2018-12-25	3	92.01	8	3	7461
13	1	2003-08-29	3	92.01	8	3	7037
14	1	2003-12-20	3	92.01	8	3	7203
15	3	2003-12-02	3	92.01	8	3	7234
16	1	2003-10-23	3	92.01	8	3	7186
17	1	2013-06-19	3	92.01	8	3	7492
18	1	2004-07-07	3	92.01	8	3	7297
19	3	2018-11-19	3	92.01	8	2	7401
20	0	2004-06-19	3	92.01	8	3	7365
21	3	2003-04-07	3	92.01	8	4	7019
22	3	2004-02-06	3	92.01	8	2	7005
23	0	2003-12-13	3	92.01	8	3	7110
54	3	2004-03-05	3	92.01	8	0	7158
55	3	2003-04-07	3	92.01	8	4	7001
56	1	2004-10-30	3	92.01	8	4	7342
57	1	2003-12-17	3	92.01	8	3	7086
58	1	2004-02-02	3	92.01	8	3	B
59	0	2003-10-10	3	92.01	8	3	c
60	1	2003-09-06	3	92.01	8	3	7339
63	1	2003-11-10	3	92.01	8	\N	7215
64	1	2004-09-19	3	92.01	8	3	7306
65	3	2003-04-07	3	92.01	8	4	7019
66	0	2003-11-19	3	92.01	8	\N	7401
67	1	2003-10-21	3	92.02	8	3	7264
68	1	2004-04-14	3	92.02	8	1	7287
69	0	2003-12-03	3	92.02	8	3	7174
70	1	2004-10-30	3	92.02	8	3	7144
71	0	2003-12-17	3	92.02	8	4	7179
72	0	2018-11-13	3	92.02	8	4	7120
73	1	2003-12-20	3	92.02	8	3	7170
74	1	2004-02-14	3	92.02	8	3	7089
75	1	2003-06-01	3	92.02	8	4	7131
76	0	2003-07-21	3	7146	8	4	7146
77	1	2003-07-02	3	92.02	8	3	7383
78	1	2004-02-27	3	92.02	8	4	7369
79	0	2003-06-01	3	92.02	8	3	7274
80	1	2003-04-29	3	92.02	8	3	7058
81	1	2004-01-24	3	9202	8	4	7002
82	1	2004-04-25	3	92.02	8	3	7117
83	1	2003-05-05	3	92.02	8	1	7078
84	0	2003-10-23	3	92.02	8	3	7203
85	0	2003-11-06	3	92.02	8	1	7245
86	0	2003-07-10	3	92.02	8	1	7196
87	0	2004-06-24	3	92.02	8	\N	7490
88	0	2003-07-05	3	92.02	8	3	7293
89	0	2004-12-07	3	92.02	8	0	7326
90	1	2004-01-24	3	92.02	8	3	A
91	1	2003-05-31	3	92.02	8	4	g
92	1	2003-08-25	3	92.02	8	1	7062
93	0	2003-11-07	3	92.02	8	4	l
94	0	2003-12-19	3	92.02	8	3	M
95	1	2004-03-17	3	92.01	8	4	7128
96	1	2003-10-21	3	92.02	8	1	7410
97	0	2018-11-13	3	92.02	8	\N	7095
98	1	2003-06-01	3	92.02	8	4	7331
99	0	2004-06-22	3	92.02	8	1	7319
100	0	2018-11-13	3	92.02	8	4	p
138	0	2003-09-08	1	92.03	2	3	5427
101	0	2003-05-15	0	92.01	2	3	5484
102	0	2004-01-12	0	92.01	2	4	5103
103	1	2003-09-18	0	92.01	2	4	5489
104	1	2004-02-15	0	92.01	2	1	5433
105	1	2004-08-08	0	92.01	2	3	5124
106	0	2004-07-25	0	92.01	2	3	5422
107	0	2004-05-13	0	92.01	2	1	5406
109	0	2018-04-03	0	92.01	2	3	5062
108	0	2004-03-29	0	92.01	2	3	5477
110	0	2004-01-20	0	92.01	2	3	5250
111	1	2003-09-13	0	92.01	2	3	5177
112	1	2004-01-26	0	92.01	2	3	5027
113	1	2003-11-06	0	92.01	2	0	5426
114	0	2018-10-22	0	92.01	2	3	5428
115	0	2003-08-05	0	92.01	2	1	5201
116	1	2003-11-30	0	92.01	2	3	5276
117	1	2003-10-22	0	92.01	2	3	5273
118	1	2018-11-05	0	92.01	2	3	5049
119	1	2002-12-26	0	92.01	2	1	5041
120	0	2001-10-23	0	92.01	2	3	5388
121	1	2003-05-05	0	92.01	2	3	5284
122	1	2004-11-05	0	92.01	2	3	5003
123	1	2003-05-15	0	92.01	2	3	5348
124	0	2003-11-20	0	92.01	2	3	5361
125	0	2018-09-10	0	92.01	2	3	5202
126	1	2004-12-28	0	92.01	2	0	5047
127	0	2004-04-24	0	92.01	2	3	5306
128	0	2004-01-05	0	92.01	2	2	5382
129	1	2003-08-23	0	92.01	2	3	5461
130	1	2003-08-10	0	92.01	2	4	5391
131	1	2004-04-04	0	92.01	2	1	5322
132	0	2004-01-12	0	92.01	2	3	5469
133	1	2003-11-05	0	92.01	2	3	5107
134	1	2003-08-31	0	92.01	2	0	5321
135	0	2004-01-27	0	92.01	2	3	5136
136	1	2004-04-12	0	92.01	2	1	5367
137	1	2004-03-09	0	92.01	2	3	5305
139	0	2004-04-24	0	92.03	2	3	5005
140	0	2004-05-10	1	92.03	2	1	5032
141	0	2002-11-27	1	92.03	2	3	5272
142	1	2002-03-12	0	92.03	2	0	5317
143	0	2004-01-12	1	92.03	2	1	5247
144	1	2004-04-24	1	92.03	2	3	5460
145	1	2003-11-05	0	92.03	2	1	5100
146	0	2003-07-29	1	92.03	2	4	5246
147	0	2002-10-08	1	92.03	2	3	5241
148	1	2004-02-21	1	92.03	2	3	5341
149	1	2002-12-15	1	92.03	2	3	5482
150	\N	2004-04-21	1	92.03	2	3	5405
151	1	2003-12-20	1	92.03	2	3	5465
152	1	2018-03-20	1	92.03	2	3	5087
153	1	2004-02-19	1	92.03	2	3	5403
154	1	2003-12-15	1	92.03	2	3	5008
155	1	2003-10-11	1	92.03	2	0	5497
156	1	2002-02-15	1	92.03	2	3	5051
157	1	2003-11-13	1	92.03	2	3	5409
158	0	2002-11-24	1	92.03	2	3	5441
159	1	2000-09-30	1	92.03	2	1	5122
160	1	2004-03-15	1	92.03	2	4	5254
161	1	2003-03-07	1	92.03	2	3	5080
162	1	2003-10-07	1	92.03	2	3	5274
163	1	2003-10-10	1	92.03	2	4	5132
164	0	2000-06-22	1	92.03	2	4	5140
165	1	2003-08-13	1	92.03	2	3	5409
166	1	2003-05-11	1	92.03	2	3	5373
168	0	2002-10-11	1	92.03	2	3	5002-A
167	0	2018-03-17	1	92.03	2	0	5002-B
170	1	2004-01-07	3	92.01	4	3	5823-B
169	1	2003-12-07	3	92.01	4	1	5823-A
171	1	2004-03-30	3	92.01	4	0	5630
172	1	2003-09-28	3	92.01	4	1	5757
173	1	2005-02-06	3	92.01	4	3	5520
174	1	2003-04-01	3	92.01	3	3	5573
175	0	2004-03-15	3	92.01	4	4	5748
176	1	2004-07-28	3	92.01	4	4	5769
177	0	2003-03-11	3	92.01	4	3	5999
178	\N	2003-11-01	3	92.01	4	3	5910
179	1	2003-10-31	3	92.01	4	1	5634
180	0	2003-06-15	3	92.01	4	3	5674
181	0	2003-12-10	3	92.01	4	1	5892
182	1	2004-01-24	3	92.01	4	3	5885
183	0	2004-01-03	3	92.01	4	3	5881
184	0	2003-11-05	3	92.01	4	4	5650
185	0	2003-08-22	3	92.01	4	4	5643
186	1	2003-08-11	3	92.01	4	3	5797
187	0	2004-01-26	3	92.01	4	2	5974
188	1	2004-06-10	3	92.01	4	1	5986
189	0	2004-07-25	3	92.01	4	0	5553
190	0	2004-10-30	3	92.01	4	3	5650
191	1	2004-03-02	3	92.01	4	0	5655
192	0	2003-08-13	3	92.01	4	1	5944
193	0	2002-10-17	3	92.01	4	1	5560
194	1	2018-10-01	3	92.01	4	3	5939
195	0	2003-08-26	3	92.01	4	3	5581
196	1	2003-11-04	3	92.01	4	1	5966
197	0	2018-12-09	3	92.01	4	2	5710
198	0	2004-04-17	3	92.01	4	1	5738
199	0	2004-08-11	3	92.01	4	1	5752
201	0	2003-10-17	3	92.01	4	4	5648
202	0	2003-12-23	3	92.01	4	4	5941
203	0	2018-11-30	3	92.01	4	1	5522
204	0	2018-01-01	3	92.01	4	3	NVC
205	0	2004-05-13	3	92.01	4	1	5720
206	1	2004-03-21	3	92.02	4	3	5638
207	1	2003-10-23	3	92.02	4	3	5606
208	0	2003-09-16	3	92.02	4	3	5514
209	3	2018-01-01	3	92.02	4	3	5612
211	1	2004-05-24	3	92.02	4	3	5999
210	0	2018-10-11	3	92.02	4	1	5923
212	0	2003-09-23	3	92.02	4	3	5615
213	1	2018-04-10	3	92.02	4	4	5524
214	1	2004-07-16	3	92.02	4	3	5576
215	0	2004-01-24	3	92.02	4	4	5764
216	1	2004-06-13	3	92.02	4	3	5616
217	1	2004-03-02	3	92.02	4	3	5981
218	1	2003-10-20	3	92.02	4	3	5979
219	1	2004-03-28	3	92.02	4	4	5689
220	0	2004-04-02	3	92.02	4	3	5505
221	1	2003-05-19	3	92.02	4	1	5708
222	0	2018-11-08	3	92.02	4	4	5550
223	0	2018-01-01	3	92.02	4	2	5808
224	0	2004-02-16	3	92.02	4	1	5536
225	0	2003-10-24	3	92.02	4	2	5698
226	0	2003-10-16	3	92.02	4	4	5742
227	0	2003-10-17	3	92.02	4	3	5677
228	0	2003-11-28	3	92.02	4	3	5608
229	1	2004-04-13	3	92.02	4	3	5724
248	0	2004-01-30	3	92.03	4	4	5576
231	0	2003-10-09	3	92.02	4	1	5816
230	0	2004-02-09	3	92.02	4	3	5815-B
200	0	2018-11-25	3	92.01	4	3	5815-A
233	1	2004-03-30	3	92.02	4	0	5850
234	1	2004-01-22	3	92.02	4	3	5781
235	1	2003-05-21	3	92.02	4	4	5733
236	1	2003-07-04	3	92.02	4	4	5747
237	0	2003-10-21	3	92.02	4	3	5503
238	1	2004-03-22	3	92.02	4	3	5507
239	1	2003-07-25	3	92.02	4	1	5929
240	0	2003-08-29	3	92.02	4	3	5976
241	1	2003-12-24	3	92.02	4	3	5661
242	0	2003-02-17	3	92.02	4	1	5606-B
243	0	2003-06-30	3	92.02	4	3	5696
244	1	2018-01-01	3	92.02	4	\N	5977
245	1	2018-11-12	3	92.02	4	\N	5734
246	0	2018-11-10	3	92.02	4	\N	5634-B
247	0	2018-11-01	3	92.02	4	\N	5647
249	1	1986-05-07	3	92.03	4	3	5661
251	0	2004-01-30	3	92.03	4	4	5567
252	0	2003-05-13	3	92.03	4	1	5689-B
253	1	2003-06-28	3	92.03	4	3	5961
254	1	2003-07-06	3	92.03	4	3	5518
255	1	2003-08-21	3	92.03	4	3	6000
256	0	2003-10-21	3	92.03	4	1	5580
257	0	2004-03-02	3	92.03	4	3	5736
259	0	2018-11-08	3	92.03	4	\N	5548
260	0	2004-07-17	3	92.03	4	1	5577
261	1	2004-01-06	3	92.03	4	0	5771
262	0	2004-02-08	3	92.03	4	3	5687
263	2	2004-03-20	3	92.03	4	3	5588
264	3	2004-07-09	3	92.03	4	0	5702
266	0	2004-02-06	3	92.03	4	0	5606-C
267	1	2003-07-08	3	92.03	4	3	5959
268	1	2003-07-20	3	92.03	4	3	5711
269	1	2004-07-28	3	92.03	4	3	5941-B
270	0	2004-02-21	3	92.03	4	3	5633
271	0	2004-01-12	3	92.03	4	1	5849
272	1	2004-05-24	3	92.03	4	4	5924
273	1	2004-03-25	3	92.03	4	3	5772
274	0	2004-10-07	3	92.03	4	4	5787
275	3	2003-08-23	3	92.03	4	1	5889
276	0	2003-09-28	3	92.03	4	3	5938
277	1	2004-02-19	3	92.03	4	3	5801
278	1	2003-11-12	3	92.03	4	3	5868
279	1	2004-01-20	3	92.03	4	3	5987
280	1	2004-03-21	3	92.03	4	3	5529
281	1	2003-11-01	3	92.03	4	4	5553-B
282	1	2004-03-29	3	92.03	4	3	5684
283	0	2003-07-07	3	92.03	4	4	5615-B
284	0	2004-07-09	0	92.01	9	3	107
285	1	2001-08-08	0	92.01	9	3	100
286	1	2001-08-10	0	92.01	9	3	143
287	1	2001-08-03	0	92.01	9	4	186
288	1	2000-02-23	0	92.01	9	3	173
289	0	2002-06-17	0	92.01	9	4	145
290	0	2004-06-01	0	92.01	9	3	187
291	0	2002-05-08	0	92.01	9	3	179
292	0	2002-05-01	0	92.01	9	4	126
293	3	2014-08-04	0	92.01	9	\N	162
294	0	2003-01-12	0	92.01	9	4	100
295	0	2001-07-27	0	92.01	9	3	148
296	1	2004-05-23	0	92.01	9	3	117
297	1	2004-08-14	0	92.01	9	3	133
298	1	2002-03-19	0	92.01	9	3	145
299	\N	2003-05-03	0	92.01	9	4	118
300	1	2018-09-14	0	92.01	9	3	184
301	1	2002-04-19	0	92.01	9	1	101
302	1	2004-05-11	0	92.01	9	4	105
303	0	2000-07-20	0	92.01	9	3	191
304	3	2003-07-07	0	92.01	9	\N	187
305	0	1999-08-06	0	92.01	9	3	101
306	1	2003-09-04	0	92.01	5	1	6878
307	1	2004-01-13	0	92.01	5	1	6869
308	0	2003-10-30	0	92.01	5	1	6746
309	1	2018-12-19	0	92.01	5	1	6593
310	1	2004-05-26	0	92.01	5	1	6713
311	0	2003-07-20	0	92.01	5	1	6861
313	0	2004-01-12	0	92.01	5	1	6625
312	1	2004-06-26	0	92.01	5	1	6774-B
315	1	2005-01-24	0	92.01	5	1	6881
316	1	2003-03-16	0	92.01	5	1	6700
317	1	2004-02-22	0	92.01	5	1	6819
318	0	2003-10-20	0	92.01	5	3	6978
319	0	2004-01-02	0	92.01	5	1	6678
329	1	2004-02-09	1	92.01	5	3	6987
330	0	2003-11-10	0	92.01	5	1	6784
333	1	2018-11-14	0	92.01	5	1	6578
335	0	2003-04-19	0	92.01	5	3	6531
336	1	2003-11-17	0	92.01	5	1	6633
337	1	2004-04-23	0	92.01	5	1	6545
338	1	2004-06-08	0	92.01	5	4	6572
339	0	2003-11-10	0	92.01	5	1	6784
341	0	2004-04-12	0	92.01	5	1	6606
342	1	2003-11-12	0	92.01	5	1	6948
343	0	2003-10-20	0	92.01	5	3	6978
345	1	2003-12-02	0	92.01	5	1	6780
346	1	2003-03-16	0	92.01	5	1	6700
347	1	2004-01-13	0	92.01	5	1	6869
328	1	2004-02-13	0	92.01	5	3	6963
349	0	2018-11-14	0	92.01	5	4	6653
320	0	2004-02-22	0	92.01	5	3	6995
350	1	2003-06-25	0	92.01	5	1	6659
351	1	2003-08-07	0	92.01	5	1	6925
352	0	2004-01-26	0	92.01	5	1	6904
353	1	2003-09-04	0	92.01	5	1	6878
327	0	2004-01-18	0	92.01	5	3	6757
354	0	2003-05-26	0	92.01	5	4	6929
355	1	2004-02-22	0	92.01	5	1	6819
369	1	2001-05-17	0	92.01	6	3	1677
357	0	2018-11-14	0	92.01	5	1	6775
356	0	2004-01-02	0	92.01	5	1	6717
358	0	2004-06-15	0	92.01	5	1	6989
359	0	2003-08-20	0	92.01	5	1	6523
331	1	2003-11-10	0	92.01	5	1	6751
314	1	2003-08-31	0	92.01	5	1	6903
334	1	2004-02-01	0	92.01	5	3	6774
360	1	2004-06-20	0	92.01	6	0	1681
361	0	2004-05-01	0	92.01	6	3	1236
362	1	2003-12-04	0	92.01	6	3	1668
364	0	2004-03-01	0	92.01	6	3	1824
365	0	2004-02-02	0	92.01	6	3	1847
366	0	2003-04-01	0	92.01	6	3	1373
367	0	2004-03-02	0	92.01	6	3	1634
368	0	2004-04-01	0	92.01	6	3	1123
370	0	2003-06-23	0	92.01	6	4	1496
371	0	2014-10-03	0	92.01	6	3	1492
372	0	2003-01-16	1	92.03	5	1	6740
373	2	2003-06-09	1	92.03	5	4	6643
374	1	2004-08-13	1	92.03	5	3	6686
375	1	2003-10-21	1	92.03	5	3	6699
376	1	2004-03-05	1	92.03	5	3	6945
378	0	2003-07-31	1	92.03	5	1	6674
379	1	2003-06-29	1	92.03	5	3	6615
380	0	2004-11-29	1	92.03	5	4	6584
381	1	2003-12-04	1	92.03	5	1	6865
382	0	2004-04-04	1	92.03	5	1	6952
383	0	2018-11-23	1	92.03	5	1	6965
384	0	2003-06-02	1	92.03	5	3	6774
386	0	2003-12-09	1	92.03	5	3	6629
387	1	2003-07-18	1	92.03	5	1	6724
385	0	2004-04-21	1	92.03	5	3	6831
388	1	2005-12-15	1	92.03	5	1	6986
389	1	2004-07-28	1	92.03	5	3	6792
390	1	2004-08-26	1	92.03	5	3	6669
391	1	2004-02-15	1	92.03	5	3	6692
392	1	2018-09-30	1	92.03	5	1	6725
393	1	2004-03-11	1	92.03	5	3	6734
394	0	2004-01-19	1	92.03	5	3	6668
395	0	2004-04-08	1	92.03	5	1	6944
396	0	2003-10-05	1	92.03	5	3	6515
397	0	2003-08-13	1	92.03	5	3	6841
398	1	2003-10-24	1	92.03	5	4	6615B
399	0	2003-09-11	1	92.03	5	1	6964
400	0	2004-04-14	1	92.03	5	0	6585
401	1	2003-08-21	1	92.03	5	3	6889
402	1	2004-08-25	1	92.03	5	4	6989-B
403	0	2004-02-28	1	92.03	5	4	6631
404	0	2004-06-03	1	92.03	5	3	6644
405	1	2004-01-17	1	92.02	5	1	6665
406	0	2004-01-03	1	92.02	5	3	6768-C
408	1	2004-02-04	1	92.02	5	1	6804
407	0	2003-11-18	1	92.02	5	3	6771-B
409	1	2018-11-19	1	92.02	5	3	6806
410	1	2003-06-25	1	92.02	5	3	6768
411	0	2004-06-25	1	92.02	5	3	6825
412	1	2003-11-11	1	92.02	5	1	6694
413	0	2004-04-16	1	92.02	5	0	6844
414	0	2002-08-03	1	92.02	5	3	6769
415	1	2004-10-01	1	92.02	5	1	6512
416	1	2003-07-21	1	92.02	5	4	6677
417	1	2003-09-03	1	92.02	5	1	6917-C
418	0	2005-05-28	1	92.02	5	3	6582
419	0	2004-03-08	1	92.02	5	\N	6917
420	1	2004-09-13	1	92.02	5	1	6917B
421	1	2018-11-23	1	92.02	5	3	6549
422	0	2004-02-20	1	92.02	5	4	6569
423	1	2003-10-10	1	92.02	5	3	6997
424	1	2003-07-09	1	92.02	5	1	6526
425	0	2003-02-09	1	92.02	5	3	6894
426	1	2003-09-13	1	92.02	5	3	6768-B
427	0	2003-12-18	1	92.02	5	4	6965B
428	1	2004-01-27	1	92.02	5	3	6505
429	1	2004-02-01	1	92.02	5	0	6644-B
430	1	2003-11-27	1	92.02	5	1	6729
431	1	2003-12-15	1	92.02	5	1	6580
432	0	2003-10-07	1	92.02	5	1	6906
433	0	2003-04-04	1	92.02	5	3	6668-B
434	0	2003-04-10	1	92.02	5	4	6663
435	0	2004-03-20	1	92.02	5	3	6741
436	1	2018-11-19	1	92.02	5	3	6818
437	1	2003-10-08	1	92.02	5	3	6641
439	1	2007-07-31	1	92.02	5	3	6734-B
440	1	2004-05-04	1	92.02	5	1	6763
441	1	2004-01-19	0	92.02	5	1	6624
442	0	2003-09-20	1	92.02	5	3	6745
443	1	2003-08-21	1	92.02	5	3	6742
444	1	2018-06-22	1	92.02	5	1	6940
445	1	2004-02-24	1	92.04	3	3	3998
446	1	2003-09-16	1	92.04	3	3	3884
447	0	2003-02-19	1	92.04	3	4	3758
448	1	2003-07-27	1	92.04	3	3	3884-B
449	0	2003-09-25	1	92.04	3	3	3964
450	0	2003-08-07	1	92.04	3	3	3194
451	1	2003-03-15	1	92.04	3	3	3183
452	1	2004-06-14	1	92.04	3	3	3298
453	1	2004-04-16	1	92.04	3	\N	3414
454	1	2004-01-06	1	92.04	3	1	3858
455	3	2004-05-18	1	92.04	3	4	3236
456	1	2005-09-19	1	92.04	3	4	3866
457	1	2003-10-06	1	92.04	3	3	3344
458	1	2003-07-09	1	92.04	3	1	3381
459	1	2004-05-05	1	92.04	3	1	3153
460	1	2003-12-10	1	92.04	3	3	3701
461	0	2018-04-28	1	92.04	3	2	3506
462	1	2018-11-08	1	92.04	3	1	3134
463	0	2003-11-17	1	92.04	3	1	3676
464	1	2004-02-10	1	92.04	3	4	3266
465	0	2004-04-07	1	92.04	3	1	3274
466	0	2004-09-12	1	92.04	2	1	3443
467	1	2004-03-02	1	92.04	3	4	3450
469	1	2003-08-14	1	92.04	3	4	3029
470	0	2004-03-24	1	92.04	3	1	3199
471	0	2004-10-02	1	92.04	3	4	3095
472	1	2004-08-30	1	92.04	3	1	3060
473	1	2007-07-27	1	92.04	3	3	3740
474	1	2004-01-27	1	92.04	3	4	3031
475	0	2004-11-18	1	92.04	3	1	3661
476	1	2004-03-24	1	92.04	3	3	3289
477	1	2003-08-27	1	92.01	3	3	3228
506	1	2004-06-12	1	92.02	6	3	HT19
478	0	2004-02-19	1	92.04	3	2	3217
468	0	2004-05-09	1	92.04	3	3	3776
479	0	2003-11-01	3	92.02	1	3	0T15
480	1	2004-09-05	0	92.02	1	\N	0Y88
481	1	2002-11-23	3	92.02	1	4	0y13
482	0	2004-04-12	3	92.02	1	\N	0Y87
483	1	2004-04-01	3	92.02	1	3	0Z14
484	1	2003-06-01	3	92.01	1	3	0T57
485	1	2003-02-13	3	92.01	1	\N	ZY34
486	1	2003-03-23	3	92.01	1	\N	5666
489	0	2002-07-02	1	92.02	6	1	HT49
490	0	2003-08-10	1	92.02	6	4	HT47
487	1	2003-07-15	1	92.02	6	0	HT09
492	1	2003-04-29	1	92.02	6	2	HT35
493	0	2003-09-18	1	92.02	6	2	HT36
494	1	2004-09-10	1	92.02	6	3	HT37
491	0	2004-03-01	1	92.02	6	1	HT34
488	1	2003-11-04	1	92.02	6	3	HT43
495	0	2003-05-02	1	92.02	6	4	HT40
496	0	2002-12-23	1	92.02	6	4	HT45
497	0	2004-03-15	1	92.02	6	4	HT29
498	3	2004-04-02	1	92.02	6	1	HT38
499	0	2002-10-16	1	92.02	6	3	HT46
500	1	2004-01-02	1	92.02	6	0	HT01
501	1	2005-08-05	1	92.02	6	1	HT31
502	1	2003-04-08	1	92.02	6	1	HT28
504	1	2003-08-21	1	92.02	6	1	HT32
505	0	2004-10-07	1	92.02	6	3	HT23
507	0	2002-06-24	1	92.02	6	1	HT16
508	1	2003-12-04	1	92.02	6	3	HT42
503	1	2003-07-27	1	92.02	6	4	HT26
509	0	2004-02-20	1	92.02	6	3	HT21
510	1	2003-11-29	1	92.02	6	3	HT11
511	1	2004-02-18	1	92.02	6	1	HT10
512	1	2003-11-17	1	92.02	6	4	HT06
513	1	2003-05-12	1	92.02	6	3	HT05
514	1	2004-05-17	1	92.02	6	3	HT04
515	1	2003-08-31	1	92.02	6	2	HT44
516	0	2003-05-19	1	92.02	6	3	HT03
517	1	2004-03-06	1	92.02	6	3	HT02
518	1	2004-06-14	1	92.02	6	0	HT25
519	1	2003-03-15	1	92.02	6	1	HT33
520	1	2018-11-06	1	92.02	6	0	HT17
522	0	2003-12-17	0	92.01	6	3	139C
523	0	2003-11-06	1	92.02	6	4	4200
524	1	2003-01-01	0	92.01	6	3	1292
525	0	2003-11-01	0	92.01	6	3	1615
526	0	2003-09-18	1	92.01	6	1	1805
527	1	2003-11-17	0	92.01	6	3	1869
528	1	2003-06-17	0	92.01	6	3	1270
529	1	2018-10-17	1	92.01	6	1	4225
530	1	2004-02-09	0	92.01	6	3	1973
531	0	2003-07-01	0	92.01	6	1	1499
532	0	2003-09-01	0	92.01	6	1	1606
533	1	2004-01-25	0	92.01	6	3	1697
534	1	2003-02-23	0	92.01	6	\N	1853
535	1	2003-10-01	0	92.01	6	3	4215
536	0	2004-04-01	0	92.01	6	1	1432
537	1	2005-01-14	0	92.01	6	3	1041
538	0	2003-07-01	0	92.01	6	0	1044
539	1	2003-08-27	0	92.01	6	0	4240
540	0	2003-08-11	0	92.01	6	3	1083
541	1	2003-12-24	0	92.01	6	3	1806
542	0	2003-07-01	0	92.01	6	1	1257
543	0	2004-01-01	0	92.01	6	3	1597
544	1	2003-08-19	0	92.01	6	3	1546
545	1	2003-02-06	0	92.01	6	1	1096
546	0	2004-02-07	0	92.01	6	0	4282
\.


--
-- Data for Name: administracao_campanha; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.administracao_campanha (id, nome) FROM stdin;
1	Pesquisa sobre saúde bucal da rede municipal de ensino de Palmas - 2018
\.


--
-- Data for Name: administracao_diretor; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.administracao_diretor (id, data, questao_1, questao_2, questao_3, questao_4, questao_5, questao_6, questao_7, questao_8, questao_9, questao_10, questao_11, questao_12, questao_13, questao_14, questao_15, questao_16, questao_17, questao_18, questao_19, questao_20, questao_21, questao_22, questao_23, questao_24, questao_25, questao_26, questao_27, questao_28, questao_29, questao_30, questao_31, questao_32, questao_33, questao_34, questao_35, questao_36, questao_37, questao_38, questao_39, questao_40, questao_41, questao_42, questao_43, questao_44, questao_45, questao_46, questao_47, questao_48, questao_49, questao_50, questao_51, questao_52, questao_53, questao_54, questao_55, questao_56, questao_57, questao_58, questao_59, questao_60, questao_61, questao_62, questao_63, questao_64, questao_65, questao_66, questao_67, questao_68, questao_69, questao_70, questao_71, questao_72, questao_73, questao_74, questao_75, questao_76, questao_77, questao_78, questao_79, questao_80, questao_81, questao_82, questao_83, questao_84, escola_id) FROM stdin;
2	\N	{0,2,3}	1	{1,3}	5	1	0	2	6	0	2	0	1	1	0	0	0	1	2	2	0	0	2	2	3	0	0	0	{0,1,2}	1	1	{0,3}	0	{0,2,3}	1	2	1	{}	0	{0,1,2,4,5}	0	0	0	0	0	0	1	0	1	4	1	0	0	8	0	8	0	8	0	1	0	1	1	\N	1	1	1	0	1	0	2	0	0	0	0	0	1	1	0	0	0	0	0	1	1	3
3	\N	{0,2}	1	{1}	4	1	0	1	1	0	2	0	4	1	0	0	0	1	2	2	1	0	2	2	0	0	0	0	{0}	0	0	{0}	0	{0,2}	0	0	1	{}	1	{}	0	0	1	0	0	0	0	0	0	4	1	0	0	8	1	\N	1	\N	0	1	1	\N	1	\N	1	1	1	0	1	0	6	0	1	0	0	1	1	0	0	0	0	0	0	0	0	2
4	\N	{1}	0	{1}	5	1	0	1	0	1	1	0	1	0	0	0	0	1	2	0	1	0	0	0	0	0	0	0	{0,1,2,4}	0	0	{0,1,2}	0	{4}	0	0	1	{}	0	{8}	1	0	0	0	0	0	0	0	1	4	1	0	0	8	0	8	0	8	0	1	1	\N	1	\N	1	1	4	0	1	0	4	0	1	0	1	0	0	1	1	0	0	0	0	0	0	8
5	\N	{0,2}	1	{1}	4	1	0	2	0	1	0	0	2	0	0	0	0	1	2	2	1	0	2	2	0	0	0	0	{0,1,2,3}	0	0	{0,1,2,3}	0	{0,2}	0	0	1	{}	0	{0,2,3,4,5,6,7,8,9}	1	0	0	0	0	0	0	0	1	4	0	0	0	8	0	9	0	9	1	1	0	1	1	\N	1	1	1	0	1	0	4	0	1	0	0	0	0	1	1	0	0	0	0	0	1	6
6	\N	{0,2}	1	{1}	4	1	0	1	1	1	2	0	3	1	0	0	0	1	2	2	0	0	0	0	0	0	0	0	{0,1,2,3,4,5}	0	0	{0,1,2,3}	0	{0,2}	0	2	1	{}	0	{0,2,4,5,6,7,8,9}	1	0	2	0	0	0	0	0	0	4	0	0	0	9	0	9	0	9	0	0	1	\N	1	\N	1	1	2	0	1	0	3	0	0	0	0	0	0	1	0	0	0	0	0	0	1	5
7	\N	{1}	0	{1}	5	3	0	0	2	0	0	0	2	0	\N	0	0	1	2	0	0	0	0	0	0	1	0	0	{0,4}	0	0	{0,1,3}	0	{4}	0	0	1	{}	1	{}	0	0	0	0	0	2	0	0	1	4	0	\N	\N	8	1	\N	\N	\N	1	0	1	1	1	\N	1	1	0	0	1	1	\N	1	0	1	1	0	0	1	1	1	0	1	1	0	1	4
8	\N	{0,2}	0	{1}	3	1	0	1	0	1	0	0	1	1	0	0	0	1	2	2	1	0	2	2	3	0	0	0	{7}	0	0	{0,1}	0	{0,2,4}	0	2	1	{}	0	{0,2,4,5,6,7,8,9,10}	0	0	0	0	0	0	0	0	0	4	0	0	0	8	0	8	0	8	0	1	0	1	1	\N	1	1	2	0	1	1	\N	1	1	0	1	1	1	1	1	0	0	0	0	0	0	1
\.


--
-- Data for Name: administracao_escola; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.administracao_escola (id, nome, acao_id, latitude, longitude) FROM stdin;
1	Escola municipal Luiz Gonzaga	1	-10.156690000000000000	-48.328120000000000000
2	Escola municipal Mestre Pacífico S. Campos	1	-10.156270000000000000	-48.344930000000000000
3	Escola municipal Beatriz Rodrigues da Silva	1	-10.163590000000000000	-48.340670000000000000
4	Escola municipal de T.I. Padre Josimo M. Tavares	1	-10.170240000000000000	-48.335380000000000000
5	Escola municipal Anne Frank	1	-10.179730000000000000	-48.311120000000000000
6	Escola municipal Henrique Talone Pinheiro	1	-10.194800000000000000	-48.310440000000000000
7	Escola municipal Antônio Carlos Jobim	1	-10.257200000000000000	-48.320970000000000000
9	Escola Silverio Ribeiro Matos	1	-10.345006700000000000	-46.571067100000000000
8	Escola municipal de T.I. Margarida Gonçalves	1	-10.331090000000000000	-48.320050000000000000
11	Escola de teste	36	-10.161814654117114000	-48.341461034979260000
\.


--
-- Data for Name: administracao_exame; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.administracao_exame (id, data, examinador, anotador, aluno_id, carie_coroa_11, carie_coroa_12, carie_coroa_13, carie_coroa_14, carie_coroa_15, carie_coroa_16, carie_coroa_17, carie_coroa_18, carie_coroa_21, carie_coroa_22, carie_coroa_23, carie_coroa_24, carie_coroa_25, carie_coroa_26, carie_coroa_27, carie_coroa_28, carie_coroa_31, carie_coroa_32, carie_coroa_33, carie_coroa_34, carie_coroa_35, carie_coroa_36, carie_coroa_37, carie_coroa_38, carie_coroa_41, carie_coroa_42, carie_coroa_43, carie_coroa_44, carie_coroa_45, carie_coroa_46, carie_coroa_47, carie_coroa_48, carie_tratamento_11, carie_tratamento_12, carie_tratamento_13, carie_tratamento_14, carie_tratamento_15, carie_tratamento_16, carie_tratamento_17, carie_tratamento_18, carie_tratamento_21, carie_tratamento_22, carie_tratamento_23, carie_tratamento_24, carie_tratamento_25, carie_tratamento_26, carie_tratamento_27, carie_tratamento_28, carie_tratamento_31, carie_tratamento_32, carie_tratamento_33, carie_tratamento_34, carie_tratamento_35, carie_tratamento_36, carie_tratamento_37, carie_tratamento_38, carie_tratamento_41, carie_tratamento_42, carie_tratamento_43, carie_tratamento_44, carie_tratamento_45, carie_tratamento_46, carie_tratamento_47, carie_tratamento_48, periodontal_bolsa_11, periodontal_bolsa_1716, periodontal_bolsa_2627, periodontal_bolsa_31, periodontal_bolsa_3736, periodontal_bolsa_4647, periodontal_calculo_11, periodontal_calculo_1716, periodontal_calculo_2627, periodontal_calculo_31, periodontal_calculo_3736, periodontal_calculo_4647, periodontal_sangramento_11, periodontal_sangramento_1716, periodontal_sangramento_2627, periodontal_sangramento_31, periodontal_sangramento_3736, periodontal_sangramento_4647) FROM stdin;
1	2018-11-15	\N	\N	80	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	9	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
2	2018-11-15	\N	\N	91	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
3	2018-11-13	\N	\N	69	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
4	2018-11-13	\N	\N	2	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
5	2018-11-13	\N	\N	13	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
6	2018-11-13	\N	\N	7	0	0	0	0	1	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	4	9	0	0	0	0	0	4	0	9	0	0	0	0	5	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	6	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
7	2018-11-13	\N	\N	70	0	0	0	0	1	1	0	9	0	0	0	1	0	0	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	4	0	9	0	0	0	0	1	1	0	9	0	0	0	5	0	0	0	9	0	0	0	0	0	9	0	9	0	0	0	0	0	9	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
8	2018-11-13	\N	\N	8	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
9	2018-11-13	\N	\N	5	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
11	2018-11-13	\N	\N	4	0	0	0	0	0	0	8	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	9	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
12	2018-11-13	\N	\N	73	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
13	2018-11-13	\N	\N	54	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
14	2018-11-13	\N	\N	95	0	0	0	0	0	1	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
15	2018-11-13	\N	\N	15	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
16	2018-11-13	\N	\N	19	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
17	2018-11-13	\N	\N	81	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
18	2018-11-13	\N	\N	22	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
19	2018-11-13	\N	\N	20	0	0	0	0	0	0	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
20	2018-11-13	\N	\N	64	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
21	2018-11-13	\N	\N	18	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
22	2018-11-13	\N	\N	12	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
23	2018-11-13	\N	\N	88	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
24	2018-11-13	\N	\N	23	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
25	2018-11-13	\N	\N	21	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
26	2018-11-13	\N	\N	16	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	5	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
27	2018-11-13	\N	\N	57	0	0	0	0	0	5	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	C	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
28	2018-11-13	\N	\N	56	0	0	0	0	0	0	8	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
29	2018-11-13	\N	\N	10	0	0	0	0	0	0	8	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
30	2018-11-13	\N	\N	11	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
31	2018-11-13	\N	\N	74	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
32	2018-11-13	\N	\N	3	0	0	0	0	0	1	8	9	0	0	0	0	0	0	8	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	9	9	0	0	0	0	0	0	9	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
33	2018-11-13	\N	\N	63	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
34	2018-11-13	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
35	2018-11-13	\N	\N	6	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
36	\N	\N	\N	77	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
37	2018-11-13	\N	\N	60	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
38	2018-11-13	\N	\N	59	0	0	0	0	0	0	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	6	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
39	\N	\N	\N	79	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
40	2018-11-13	\N	\N	58	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
41	2018-11-13	\N	\N	82	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
42	2018-11-13	\N	\N	67	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
43	2018-11-13	\N	\N	83	0	0	0	5	0	0	0	9	0	0	0	5	0	0	0	8	0	0	0	0	0	0	1	9	0	0	0	0	0	3	1	9	0	0	0	9	0	0	0	9	0	0	0	9	0	0	0	0	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
44	2018-11-13	\N	\N	68	0	1	0	0	0	0	0	9	0	1	0	0	0	0	0	9	0	0	0	0	8	0	0	9	0	0	0	0	8	0	0	9	0	1	0	0	0	0	0	9	0	1	0	0	0	0	0	9	0	0	0	0	9	0	0	9	0	0	0	0	9	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
45	2018-11-13	\N	\N	86	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
46	2018-11-13	\N	\N	78	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
47	2018-11-13	\N	\N	85	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
10	2018-11-13	\N	\N	84	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	0	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
48	2018-11-13	\N	\N	87	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
49	2018-11-13	\N	\N	89	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
50	2018-10-21	\N	\N	96	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
51	2018-11-13	\N	\N	93	0	0	0	0	0	0	0	9	2	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	0	9	1	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	1	0	0	0	0	0	0	0
52	2018-11-13	\N	\N	90	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
53	\N	\N	\N	94	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
54	2018-11-13	\N	\N	97	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
55	2018-11-13	\N	\N	71	0	0	0	0	0	0	0	9	0	0	8	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
56	2018-11-13	\N	\N	98	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
57	2018-11-13	\N	\N	72	0	0	0	1	0	1	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	3	1	9	0	0	0	0	0	1	1	9	0	0	0	1	0	1	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
60	2018-11-13	\N	\N	100	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
58	2018-11-13	\N	\N	76	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
59	\N	\N	\N	99	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
61	2018-11-05	\N	\N	101	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	5	0	9	0	0	0	0	0	5	0	9	0	0	0	0	0	5	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
62	2018-11-05	\N	\N	102	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
63	2018-11-05	\N	\N	103	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	2	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	5	1	9	0	0	0	0	0	1	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
64	2018-11-05	\N	\N	105	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
65	2018-11-05	\N	\N	104	0	1	4	0	0	4	0	9	0	0	4	0	0	4	1	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	1	9	0	0	9	0	9	0	0	9	0	0	9	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
66	2018-11-05	\N	\N	107	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
67	2018-11-05	\N	\N	106	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
68	2018-11-05	\N	\N	108	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
69	2018-11-05	\N	\N	110	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
70	2018-11-05	\N	\N	109	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
71	2018-11-05	\N	\N	112	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
72	2018-11-05	\N	\N	113	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
73	2018-11-05	\N	\N	114	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	2	1	9	0	0	2	0	0	2	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	1	0	0	0	0	1	1	0	0	0	0
74	2018-11-05	\N	\N	117	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
75	2018-11-05	\N	\N	119	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	2	1	9	0	0	0	0	0	2	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	1	0	0	0	0	1	1	0	0	0	0
76	2018-11-05	\N	\N	120	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	1	0	0	0	0	1	1	0	0	0	0
77	2018-11-05	\N	\N	122	0	0	0	0	0	0	1	9	0	0	0	0	1	1	0	9	0	0	0	0	0	3	5	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	1	9	0	0	0	0	5	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
78	2018-11-05	\N	\N	123	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
79	2018-11-05	\N	\N	125	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
80	2018-11-05	\N	\N	126	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
81	2018-11-05	\N	\N	127	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
82	2018-11-05	\N	\N	118	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
83	2018-11-05	\N	\N	129	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
84	2018-11-05	\N	\N	130	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
85	2018-11-05	\N	\N	131	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
86	2018-11-05	\N	\N	133	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
87	2018-11-05	\N	\N	134	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
88	2018-11-05	\N	\N	135	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
89	2018-11-05	\N	\N	137	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
90	2018-11-05	\N	\N	138	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
91	2018-11-05	\N	\N	140	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	9	9	9	9	9	9	0	1	0	0	0	0	0	0	0	0	0	0
92	2018-11-05	\N	\N	141	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
93	2018-11-05	\N	\N	143	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
94	2018-11-05	\N	\N	146	0	0	0	0	0	0	0	9	0	0	0	3	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
95	2018-11-05	\N	\N	147	0	1	0	0	0	4	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	1	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
96	2018-11-05	\N	\N	148	0	1	0	0	0	0	0	9	0	8	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	1	0	0	0	0	0	9	0	9	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
213	2018-11-18	\N	\N	278	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
214	2018-11-08	\N	\N	279	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
97	2018-11-05	\N	\N	145	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	8	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	9	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
98	2018-11-05	\N	\N	144	0	0	0	3	5	3	1	9	0	0	0	3	3	3	1	9	0	0	0	0	5	3	3	9	0	0	0	5	0	3	3	9	0	0	0	0	9	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	9	0	0	9	0	0	0	9	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
99	2018-11-05	\N	\N	142	0	0	0	0	0	1	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	5	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	5	9	0	0	0	0	0	1	5	9	9	9	9	9	9	9	0	1	0	0	0	0	0	1	0	0	0	0
100	2018-11-05	\N	\N	149	3	0	0	3	3	2	0	9	0	0	0	3	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
101	2018-11-05	\N	\N	153	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
102	2018-11-05	\N	\N	151	0	1	0	0	0	0	0	9	0	1	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	1	0	0	0	0	0	9	0	1	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
103	2018-11-05	\N	\N	154	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
104	2018-11-05	\N	\N	156	0	0	0	0	4	4	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	4	9	0	0	0	0	0	3	3	9	0	0	0	0	6	0	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	6	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
105	2018-11-05	\N	\N	155	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
106	2018-11-07	\N	\N	159	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
107	2002-11-24	\N	\N	158	0	3	0	0	3	3	0	9	3	0	0	1	0	2	0	9	0	0	0	0	0	4	3	9	0	0	0	0	0	4	3	9	0	0	0	0	0	0	0	9	0	0	0	1	0	2	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
108	2018-11-07	\N	\N	161	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
109	2018-11-07	\N	\N	163	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	2	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	2	0	2	0	0	0	1	0	1	0
110	2000-06-22	\N	\N	164	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	4	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	1	0	0	9	9	9	9	9	9	0	2	0	0	0	2	0	1	0	0	0	1
111	2018-11-07	\N	\N	165	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	2	0	0	0	0	0	1	0	0	0
112	2018-11-05	\N	\N	162	3	0	0	0	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
113	2018-11-07	\N	\N	160	0	0	0	0	0	0	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
114	2018-11-07	\N	\N	167	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
115	2018-11-07	\N	\N	168	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
116	2018-11-06	\N	\N	170	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
117	2018-11-06	pollyanna	nathana	169	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	1	1	0	0	0
118	2018-11-06	Pollyanna	Nathane	172	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
119	2018-11-06	pollyanna	nathana	171	3	0	0	0	3	3	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	4	1	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
120	2018-11-06	\N	\N	173	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
121	2018-11-06	\N	\N	175	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	2	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
122	2018-11-06	\N	\N	174	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
123	2018-11-06	\N	\N	176	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
124	2018-11-06	pollyanna	nathana	177	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	6	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
125	2018-11-06	pollyanna	nathana	178	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
126	2018-11-06	\N	\N	179	0	0	0	6	0	3	1	9	0	0	0	6	3	3	0	9	0	0	0	6	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
127	2018-11-06	\N	\N	180	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
128	2057-11-07	\N	\N	182	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
129	2018-11-08	\N	\N	181	0	0	0	0	0	0	0	9	0	0	0	0	0	1	8	9	0	0	0	0	0	3	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	9	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
130	2018-11-06	\N	\N	183	0	0	0	0	0	0	0	9	0	0	0	1	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	1	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
131	2018-11-06	\N	\N	185	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
132	2018-11-08	\N	\N	184	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
133	2003-11-06	pallyonna	nathana	186	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
134	2018-11-06	\N	\N	187	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	1	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	1	0	1	0	0
135	2018-11-06	\N	\N	188	0	0	0	0	0	3	0	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
136	1988-11-06	\N	\N	189	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
138	2018-11-07	\N	\N	190	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	3	1	9	0	0	0	0	8	3	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	1	9	0	0	0	0	9	0	1	9	9	9	9	9	9	9	0	1	1	1	0	0	0	0	0	0	0	0
137	2018-11-06	pollyanna	nathana	191	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
139	2018-11-06	Pollyanna	Nathane	192	0	0	0	0	0	0	0	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
141	2018-11-06	pollyanna	nathana	193	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
140	2018-11-06	pollyanna	nathana	194	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	1	1	0	0	0
142	2018-11-06	\N	\N	195	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0
143	2018-11-06	Millena de Costa Siva	\N	196	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
144	2018-11-06	\N	\N	197	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
145	2018-10-06	\N	\N	199	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
146	2018-11-06	\N	\N	198	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	1	0	0
147	2018-11-06	pollyanna	nathana	200	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	D	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
148	2018-11-06	\N	\N	203	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
149	2018-11-06	\N	\N	202	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	1	0	0
150	2018-11-06	Thawan Pantio N. da Silva	\N	201	0	0	0	1	1	1	0	9	0	0	0	0	0	4	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	4	0	9	0	0	0	1	1	1	0	9	0	0	0	0	0	6	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	6	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
151	2018-11-06	\N	\N	204	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
152	2018-11-06	\N	\N	205	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
153	2018-11-08	\N	\N	207	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
154	2018-11-08	Luiz	Paulo	206	0	0	0	9	0	0	0	9	0	0	0	9	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	9	0	0	0	9	0	0	0	9	0	0	0	9	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
155	2018-11-08	\N	\N	208	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
156	2018-11-08	\N	\N	212	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
157	2018-11-08	Raguel Barbosa Dos Santos	\N	213	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
158	2018-11-08	\N	\N	214	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
159	2018-11-08	\N	\N	216	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
160	2018-11-06	\N	\N	217	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
161	2018-11-08	\N	\N	218	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
162	2018-11-08	\N	\N	220	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
163	2018-11-08	\N	\N	221	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
164	2018-11-08	\N	\N	222	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
165	2018-11-08	\N	\N	219	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
166	2018-05-08	Louis	Paulo	224	0	8	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	9	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
167	2018-11-08	\N	\N	225	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
168	2018-11-08	\N	\N	226	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
169	2018-11-08	\N	\N	227	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
170	2018-11-08	\N	\N	228	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
172	2018-11-08	\N	\N	231	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
173	2018-11-08	Luiz	Paulo	233	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	1	0	0	0	0	0	0	0	0	0
171	2018-11-08	\N	\N	230	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
174	2018-11-08	\N	\N	234	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
175	2018-11-08	\N	\N	235	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
176	2018-11-08	Luiz	Paulo	236	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	8	0	0	0	0	9	0	0	8	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	9	0	0	0	0	9	0	0	9	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
177	2018-11-08	Luis Felipe Da Silva	\N	237	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
178	2018-11-08	Jonas Vinicius Lopes Andrade	\N	240	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
179	2018-11-08	Luiz	Paulo	239	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
180	1991-11-08	\N	\N	241	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
181	2018-11-08	\N	\N	243	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
182	2018-11-08	\N	\N	245	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
183	2018-11-08	\N	\N	246	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
184	2018-11-06	\N	\N	244	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
185	2018-11-08	\N	\N	247	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
186	2018-11-18	\N	\N	248	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
187	2018-01-01	\N	\N	249	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
188	2018-11-18	\N	\N	251	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
189	2018-11-19	\N	\N	252	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
190	2018-01-01	\N	\N	253	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
191	2018-11-19	\N	\N	254	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
192	2018-11-18	\N	\N	255	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
193	2018-11-19	\N	\N	256	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
194	2018-01-01	\N	\N	257	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
195	2018-11-18	\N	\N	259	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
196	2018-11-19	\N	\N	260	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
197	2018-11-18	\N	\N	261	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
198	2018-01-01	\N	\N	262	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
199	2018-11-19	\N	\N	263	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
200	2018-11-18	\N	\N	264	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
201	2018-11-18	\N	\N	266	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
202	2018-11-19	\N	\N	267	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
203	2018-11-18	\N	\N	268	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
204	2018-11-18	\N	\N	269	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
205	2018-11-08	\N	\N	270	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
206	2018-11-18	\N	\N	271	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
207	2018-11-18	\N	\N	272	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
208	2018-11-08	\N	\N	273	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
209	2018-11-18	\N	\N	274	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
210	2003-11-18	\N	\N	275	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
211	2018-11-19	\N	\N	276	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
212	2018-11-18	\N	\N	277	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
215	2018-11-18	\N	\N	280	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
216	2018-11-08	\N	\N	281	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
217	2017-11-18	\N	\N	282	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
218	2018-11-18	\N	\N	283	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
219	2004-07-09	Ana Paula	\N	284	0	0	4	0	0	0	4	8	0	0	0	0	0	3	0	8	0	0	0	0	0	1	0	8	0	0	0	0	0	2	8	8	0	0	9	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	0	0	0	0	0	0	0	1	0	0	9	9	9	9	9	9	0	2	2	0	0	2	0	1	1	0	0	0
220	2018-09-14	\N	\N	286	0	0	0	0	0	0	0	8	0	0	0	0	0	3	0	0	0	0	0	0	0	1	0	8	0	0	0	0	0	1	0	8	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	1	0	0	9	9	9	9	9	9	0	2	2	2	2	2	1	0	1	1	1	0
221	2018-09-14	\N	\N	285	0	0	0	0	0	1	1	8	1	0	1	1	0	2	0	8	0	0	0	0	0	4	2	0	0	0	0	0	0	1	1	8	0	0	0	0	0	1	1	0	1	0	1	2	0	2	0	0	0	0	0	0	0	9	2	0	0	0	0	0	0	6	2	0	0	3	3	0	4	0	0	0	0	0	0	0	0	0	0	0	1	0
222	2018-09-14	\N	\N	288	0	0	0	0	0	1	1	8	0	0	0	0	0	4	1	8	0	0	0	0	0	3	2	8	0	0	0	0	0	1	1	8	0	0	0	0	0	6	2	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	2	0	0	0	0	0	0	1	1	0	9	9	9	9	9	9	0	2	2	2	2	2	0	1	1	1	1	1
223	2018-09-14	\N	\N	290	0	0	0	0	0	0	0	8	0	0	0	0	0	1	0	8	0	0	0	0	0	0	0	8	0	0	0	0	0	1	0	8	0	0	0	0	0	0	0	8	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	2	2	0	2	2	0	0	0	1	1	1
224	2008-09-14	\N	\N	289	0	0	0	0	0	0	0	8	0	0	0	0	0	1	1	8	0	0	0	0	0	1	1	8	0	0	0	0	0	1	1	8	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	2	2	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	2	2	2	2	2	2	1	1	1	0	0	0
225	2018-09-14	pollyanna	\N	292	0	0	0	0	0	0	0	8	0	0	0	1	1	1	1	8	0	0	0	0	0	1	1	8	0	0	1	0	1	1	1	8	0	0	0	0	0	0	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	2	5	0	0	0	1	0	1	1	1	0	9	9	9	9	9	9	0	0	0	0	2	2	0	0	0	0	0	1
226	2018-09-14	\N	\N	293	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
227	2018-09-14	\N	\N	291	0	0	0	0	0	0	0	8	0	0	0	0	0	0	1	0	0	0	0	0	0	1	1	8	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	2	0	1	1	1	1	1
228	2018-09-14	\N	\N	294	0	3	0	0	0	1	1	9	2	1	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	2	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	6	1	9	9	9	9	9	9	9	0	0	0	0	0	2	0	1	0	0	0	1
229	2018-09-14	\N	\N	295	0	0	0	0	0	0	0	0	0	0	0	0	0	2	0	9	0	0	0	0	0	1	1	0	0	0	0	0	1	1	0	8	0	0	0	0	0	0	0	0	0	0	0	0	0	5	0	9	0	0	0	0	0	1	5	0	0	0	0	0	5	6	0	0	9	9	9	9	9	9	2	2	2	2	2	2	1	1	1	0	1	1
230	2018-09-14	\N	\N	297	0	0	0	0	0	0	0	9	0	0	0	0	1	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	1	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
231	2018-09-14	\N	\N	296	0	0	0	8	8	1	1	9	0	0	0	8	8	4	1	8	1	0	0	0	0	1	1	8	1	1	0	1	1	4	1	8	0	0	0	0	0	6	1	0	0	0	0	0	0	0	1	0	2	0	0	0	0	6	1	0	2	2	0	1	1	9	1	0	0	X	X	0	0	0	2	X	X	0	2	2	0	X	X	0	1	1
232	2018-03-14	\N	\N	298	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	2	0	9	0	0	0	0	0	2	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	2	0	9	9	9	9	9	9	9	0	0	2	0	0	0	0	0	0	0	0	0
233	2018-09-14	\N	\N	301	0	0	0	0	0	0	0	8	0	0	0	0	0	3	0	8	0	0	0	0	0	3	0	8	0	0	0	0	0	0	3	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	1
234	2018-05-14	DAVID	\N	302	1	0	0	0	2	1	1	8	0	1	0	0	0	6	0	8	0	0	0	0	0	3	1	8	0	0	0	0	0	6	1	8	2	0	0	0	2	2	1	0	0	1	0	0	0	0	0	9	0	0	0	0	0	0	2	9	0	0	0	0	0	0	1	0	9	9	9	9	9	9	0	0	0	0	0	0	0	1	0	0	0	0
236	2018-09-14	\N	\N	304	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
235	2018-09-14	\N	\N	303	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
237	2018-09-14	\N	\N	305	0	0	0	0	0	1	0	8	0	0	0	0	0	1	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	4	1	0	0	0	0	0	0	1	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	6	0	0	0	0	0	0	0	0	2	0	0	0	0	0	0	0	0	0	2	0	2	2	0	0	0	0	1	1
238	2018-11-14	\N	\N	306	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
239	2018-11-14	\N	\N	307	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
240	2018-11-18	\N	\N	308	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
242	2018-11-14	\N	\N	311	T	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
243	2018-09-14	\N	\N	313	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
245	2018-11-14	\N	\N	310	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
247	2018-11-14	\N	\N	315	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
248	2018-11-14	\N	\N	316	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	2	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
249	2018-11-14	\N	\N	317	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
250	2018-11-14	\N	\N	318	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
251	2018-11-14	\N	\N	319	0	0	0	0	0	0	0	9	0	0	0	0	0	4	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
254	2018-11-14	\N	\N	320	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
241	2018-11-14	\N	\N	309	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
252	2018-11-14	\N	\N	327	0	0	0	5	0	0	0	9	0	0	0	5	0	0	0	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	9	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
246	2018-11-14	\N	\N	314	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
244	2018-11-14	\N	\N	312	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
255	2003-11-10	\N	\N	330	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
257	2018-11-14	\N	\N	329	0	0	0	0	0	0	8	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
258	2018-11-14	\N	\N	333	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
259	2018-11-14	\N	\N	335	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
260	2018-11-14	\N	\N	336	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
261	2018-11-19	\N	\N	337	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
262	2018-11-14	\N	\N	339	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
290	2018-10-02	\N	\N	368	0	0	0	5	0	0	0	9	0	0	0	5	0	0	0	9	0	0	0	5	0	0	0	9	0	0	0	5	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	1	0	0
264	2018-11-14	\N	\N	338	0	0	0	0	0	0	0	9	0	0	0	0	1	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	1	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
265	2018-11-14	\N	\N	341	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
266	2018-11-14	\N	\N	342	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
267	2018-11-14	\N	\N	343	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
269	2018-11-19	\N	\N	345	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
270	2018-11-14	\N	\N	346	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	2	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	1	9	\N	\N	\N	\N	\N	\N	\N	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
271	2018-11-14	\N	\N	347	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
253	2018-11-14	\N	\N	328	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
273	2018-11-23	\N	\N	349	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
274	2018-11-19	\N	\N	350	0	0	0	0	0	3	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	2	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
275	2004-01-26	\N	\N	352	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
276	2018-11-14	\N	\N	351	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	2	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
277	2018-11-14	\N	\N	354	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	3	3	9	\N	\N	\N	\N	\N	3	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	0	0	9	\N	\N	\N	\N	\N	0	\N	9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
279	\N	\N	\N	355	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
280	2018-11-14	\N	\N	356	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	4	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	0	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
281	2018-11-14	\N	\N	358	0	0	0	0	0	3	6	9	0	0	0	0	0	3	6	9	0	0	0	0	0	3	6	9	0	0	0	0	0	3	6	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
282	2018-11-23	\N	\N	357	0	0	0	0	0	0	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
278	2018-11-14	\N	\N	331	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	3	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	0	\N	9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
283	2018-11-23	\N	\N	359	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
284	2018-10-17	\N	\N	360	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
285	2018-10-17	\N	\N	362	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
286	2018-10-02	\N	\N	364	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
287	2018-10-02	\N	\N	361	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	2	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
288	2018-10-02	\N	\N	366	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
289	2018-10-02	\N	\N	367	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
291	2018-10-02	\N	\N	369	0	0	0	5	3	3	0	8	0	1	0	5	0	0	1	8	0	0	0	0	0	0	1	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	8	0	1	0	0	0	0	1	8	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	1	0	1	0	0	1	0	0	1	0	0
292	2018-10-02	\N	\N	365	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
293	2018-10-02	\N	\N	370	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
294	2018-10-02	\N	\N	371	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
295	2018-11-23	\N	\N	373	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
296	2018-11-23	\N	\N	374	0	0	0	0	3	3	1	9	0	1	1	0	3	3	0	9	0	0	0	0	1	0	1	9	0	0	0	0	1	0	1	9	0	0	0	0	3	3	1	9	0	1	1	0	3	3	0	9	0	0	0	0	1	0	1	9	0	0	0	0	1	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
297	2020-11-23	\N	\N	375	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	3	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
298	2018-11-23	\N	\N	376	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
299	2018-11-23	\N	\N	378	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
300	2018-11-23	\N	\N	380	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
301	2018-11-23	\N	\N	381	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
302	2018-11-23	\N	\N	379	0	0	0	3	3	1	3	9	0	0	0	3	3	0	3	9	0	0	0	3	0	0	3	9	0	0	0	3	3	0	3	9	0	0	0	3	3	1	3	9	0	0	0	3	3	0	3	9	0	0	0	3	0	0	3	9	0	0	0	3	3	0	3	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
303	2018-11-23	\N	\N	382	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	5	0	0	9	0	0	0	0	5	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
304	2018-11-23	\N	\N	384	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
305	2018-11-23	\N	\N	387	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
306	2018-11-23	\N	\N	383	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	1	0	0	1	0	0	1	0	0	1	0	0
307	2018-11-23	\N	\N	386	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
308	2018-11-23	\N	\N	388	0	0	0	0	1	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	0	9	0	0	0	0	1	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	1	1	0	1	0	0	1	0	0	1	0	0
309	2018-11-23	\N	\N	390	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
310	2018-11-23	\N	\N	391	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
311	2018-11-23	\N	\N	392	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
312	2018-11-23	\N	\N	393	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	3	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
313	2018-11-23	\N	\N	395	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
314	2018-11-23	\N	\N	394	\N	\N	\N	\N	\N	1	\N	9	\N	\N	\N	\N	\N	1	\N	9	\N	\N	\N	\N	\N	4	\N	9	\N	\N	\N	\N	\N	4	\N	9	\N	\N	\N	\N	\N	1	\N	9	\N	\N	\N	\N	\N	5	\N	9	\N	\N	\N	\N	\N	9	\N	9	\N	\N	\N	\N	\N	9	\N	9	9	9	9	9	9	9	0	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N
315	2018-11-23	\N	\N	396	0	0	0	0	0	0	0	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
316	2018-11-23	\N	\N	397	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
317	2003-10-24	\N	\N	398	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
318	2018-11-23	\N	\N	399	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
319	2018-11-23	\N	\N	400	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
320	2018-11-23	\N	\N	401	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
321	2018-11-23	\N	\N	402	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
322	2018-11-23	\N	\N	403	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
323	2018-11-23	\N	\N	404	0	0	0	5	0	0	0	9	0	0	0	5	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	1	0	0	1	0	0
324	2018-11-23	\N	\N	405	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
325	2018-11-23	\N	\N	406	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
326	2018-11-23	\N	\N	408	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	1	0	0	0	0	0	0	0	0	0
327	0218-11-23	\N	\N	411	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
328	2018-11-23	\N	\N	412	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
329	2018-11-23	\N	\N	413	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	5	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	1	1	0	0	0	0	0	0	0	0
330	2027-11-23	\N	\N	414	0	0	0	0	0	1	1	0	0	0	0	2	0	1	1	3	0	0	0	0	0	3	1	1	0	0	0	0	0	2	4	8	0	0	0	0	0	5	1	0	0	0	0	1	0	5	1	0	0	0	0	0	0	0	1	1	0	0	0	0	0	1	5	0	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
331	2018-11-23	\N	\N	415	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
332	2018-11-23	\N	\N	416	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	\N	\N	\N	\N	\N	3	3	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	0	\N	9	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	0	0	9	\N	\N	\N	\N	\N	\N	\N	9	9	9	9	9	9	9	\N	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N
333	2018-09-23	\N	\N	417	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
335	2018-11-23	\N	\N	418	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
336	2018-11-23	\N	\N	420	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
337	2018-11-23	\N	\N	421	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
338	2018-11-23	\N	\N	422	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
339	2018-11-23	\N	\N	423	0	0	0	0	0	0	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
340	2018-11-23	\N	\N	425	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
334	2018-11-23	\N	\N	419	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
341	2018-11-23	\N	\N	428	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
342	2018-11-23	\N	\N	430	0	0	8	0	0	0	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	9	0	0	0	0	5	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
343	2018-11-23	\N	\N	431	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
344	2018-11-23	\N	\N	433	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
345	2018-11-23	\N	\N	434	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
346	2018-11-23	\N	\N	432	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
347	2018-11-23	\N	\N	443	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	6	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	1	0	0	0	0	0
348	2018-11-23	\N	\N	444	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	8	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
349	2018-11-08	\N	\N	445	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
350	2018-11-08	\N	\N	446	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	1	1	0	0	0	0	0	0	0	0	0
351	2018-11-08	\N	\N	447	0	0	0	\N	1	3	1	9	0	0	1	1	1	3	1	9	0	0	0	0	0	3	1	9	0	0	0	0	1	3	4	9	0	0	0	0	0	0	1	9	0	0	0	1	1	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	1	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
352	2018-11-08	\N	\N	448	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	6	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
353	2018-11-08	\N	\N	449	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
354	2018-11-08	\N	\N	450	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	3	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	5	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
355	2018-11-08	\N	\N	451	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	1	0
356	2018-11-08	\N	\N	452	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
357	2018-11-08	\N	\N	453	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
358	2018-11-08	\N	\N	454	0	0	0	0	0	3	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	3	3	9	0	0	0	0	0	0	1	9	0	0	0	0	0	5	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
359	2018-11-08	\N	\N	455	0	0	0	0	0	0	8	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	9	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
360	2018-11-08	\N	\N	456	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
361	2018-11-08	\N	\N	457	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	9	9	9	9	9	9	1	0	0	1	0	0	1	0	0	0	0	0
362	2018-11-08	\N	\N	458	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
363	2018-11-08	\N	\N	459	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
364	2018-11-08	\N	\N	460	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
365	2018-11-08	\N	\N	461	0	0	0	3	3	1	0	9	0	0	0	0	0	8	1	9	0	0	0	0	0	3	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	5	0	9	0	0	0	0	0	6	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	5	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
366	2018-11-08	\N	\N	462	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
367	2018-11-08	\N	\N	463	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
368	2018-10-02	\N	\N	465	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
369	2018-11-08	\N	\N	464	0	0	0	6	6	0	0	9	0	0	0	6	6	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
370	2018-11-08	\N	\N	466	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
371	2018-11-08	\N	\N	467	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
372	2018-11-08	\N	\N	468	0	0	0	0	0	0	0	9	1	0	0	0	0	0	8	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	1	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
373	2018-11-08	\N	\N	469	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
374	2004-01-01	\N	\N	470	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	1	0
375	2018-11-08	\N	\N	471	3	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
376	2018-11-08	\N	\N	472	0	0	0	0	3	0	1	9	0	0	0	0	3	0	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
377	2018-11-08	\N	\N	473	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	1	0	0
378	2018-11-08	\N	\N	474	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
379	2018-11-08	\N	\N	475	0	0	0	0	0	3	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	3	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	1	0	0
380	2018-11-08	\N	\N	477	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	1	1
381	2018-11-08	\N	\N	478	1	0	0	1	0	0	0	9	1	1	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	1	0	0	1	0	0	0	9	1	1	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
382	2018-09-17	\N	\N	480	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
383	2018-10-01	\N	\N	482	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
384	2018-09-17	\N	\N	485	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
385	2018-09-17	\N	\N	486	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
386	2018-11-09	\N	\N	487	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
387	2018-11-09	\N	\N	488	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
388	2018-11-09	\N	\N	489	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
389	2018-11-09	\N	\N	490	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	1	1	1	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	1	0	9	0	0	0	0	1	1	1	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
390	2018-11-09	\N	\N	491	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
391	2018-11-09	\N	\N	492	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
392	2003-09-18	\N	\N	493	0	0	0	1	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	1	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
393	2018-11-09	\N	\N	494	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
394	2018-11-09	\N	\N	495	0	0	0	0	0	0	0	9	1	1	0	0	0	0	0	9	0	0	5	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	1	1	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	1	0	0	1	0	0
395	2018-11-09	\N	\N	496	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	8	0	0	0	0	0	0	0	8	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	8	0	0	0	0	0	0	0	8	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
396	2018-11-09	\N	\N	497	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	5	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	1	0	1	0	0	1	1	1	1	1	0
397	2018-11-09	\N	\N	498	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
398	2018-11-09	\N	\N	499	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
399	2018-11-09	\N	\N	500	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
400	2018-11-09	\N	\N	501	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
401	2018-12-09	\N	\N	502	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
402	2018-11-09	\N	\N	503	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
403	2018-11-09	\N	\N	504	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
404	2018-11-09	\N	\N	505	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
405	2018-11-09	\N	\N	507	0	0	0	0	0	0	0	9	0	0	0	0	0	0	5	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
406	2018-11-09	\N	\N	506	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
407	2018-11-09	\N	\N	509	0	0	0	0	0	2	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
408	2018-11-09	\N	\N	508	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
409	2018-11-09	\N	\N	511	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
410	2018-11-09	\N	\N	510	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
411	2018-11-09	\N	\N	512	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
412	2018-11-09	\N	\N	513	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
413	2018-11-09	\N	\N	514	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	1	1	1	0	0	0	1	1	0	0
414	2018-11-09	\N	\N	515	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
416	2018-11-09	\N	\N	516	0	0	0	0	0	0	1	9	0	0	0	0	0	0	3	9	0	0	0	0	0	1	2	9	0	0	0	0	0	1	2	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	1	9	0	0	0	0	0	1	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	1	0
415	2018-11-09	\N	\N	517	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
417	2018-11-09	\N	\N	518	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
418	2018-11-09	\N	\N	519	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
419	2018-11-09	\N	\N	520	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	1	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	1	0	0	1	0	0
421	2018-10-17	\N	\N	522	0	0	0	0	0	0	6	9	0	0	0	0	0	0	6	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	6	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	1	0	0	0	0	0	1	0	0	0	0
422	2018-10-17	\N	\N	524	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
423	2018-10-17	\N	\N	525	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
424	2018-10-02	\N	\N	527	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	2	1	9	0	0	0	0	0	2	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	5	1	9	0	0	0	0	0	5	0	9	9	9	9	9	9	9	0	0	1	0	0	0	0	0	1	1	0	0
425	2018-10-17	\N	\N	528	0	0	0	0	0	0	0	9	0	0	0	8	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	2	0	0	9	0	0	0	9	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	1	1	0	1	0	0
426	2018-10-02	\N	\N	530	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	3	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
427	2018-10-17	\N	\N	531	0	3	0	3	3	0	1	9	0	0	0	3	3	3	1	9	1	0	0	3	3	3	3	9	0	0	0	3	3	3	3	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	1	9	1	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	1	0	0	1	0	0
428	\N	\N	\N	532	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	1	0	0	0	0	0	1	0	0	0
429	2018-10-02	\N	\N	533	0	0	0	3	0	3	0	9	0	8	0	3	0	3	0	9	0	0	0	0	3	3	0	9	0	0	0	0	3	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	1	0	0	0	0
430	2018-10-17	\N	\N	534	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
431	2018-10-17	\N	\N	536	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	1	0	0	0	0	0	0	0	0
432	2018-10-17	\N	\N	537	0	0	0	0	0	3	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	2	0	9	0	0	0	0	0	3	0	0	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	1	0	9	0	0	0	0	0	0	0	0	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
433	2018-10-17	\N	\N	538	0	0	0	0	0	0	0	9	0	0	0	0	0	3	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
434	2028-10-17	\N	\N	540	3	3	0	0	0	3	0	9	3	0	0	1	0	0	0	9	3	0	0	0	0	3	0	9	0	3	3	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	8	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	1	0	0
435	2018-10-17	\N	\N	541	3	0	0	0	0	0	0	9	3	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	1	1	0	0	0	0	1	0	0	0	0
436	2018-10-02	\N	\N	542	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
437	2018-10-17	\N	\N	543	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	1	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
438	2018-10-17	\N	\N	544	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
439	2003-06-01	\N	\N	545	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	0	0	0	0	0	0	0	9	9	9	9	9	9	9	0	0	0	0	0	0	0	0	0	0	0	0
\.


--
-- Data for Name: administracao_questionario; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.administracao_questionario (id, aluno_id, questao_1, questao_10, questao_100, questao_101, questao_102, questao_103, questao_104, questao_105, questao_106, questao_107, questao_108, questao_109, questao_11, questao_110, questao_111, questao_112, questao_113, questao_114, questao_115, questao_116, questao_117, questao_118, questao_119, questao_12, questao_120, questao_121, questao_122, questao_123, questao_124, questao_125, questao_126, questao_127, questao_128, questao_129, questao_13, questao_130, questao_131, questao_132, questao_133, questao_134, questao_135, questao_136, questao_137, questao_138, questao_139, questao_14, questao_140, questao_141, questao_142, questao_143, questao_144, questao_145, questao_146, questao_15, questao_16, questao_17, questao_18, questao_19, questao_2, questao_20, questao_21, questao_22, questao_23, questao_24, questao_25, questao_26, questao_27, questao_28, questao_29, questao_3, questao_30, questao_31, questao_32, questao_33, questao_34, questao_35, questao_36, questao_37, questao_38, questao_39, questao_4, questao_40, questao_41, questao_42, questao_43, questao_44, questao_45, questao_46, questao_47, questao_48, questao_49, questao_5, questao_50, questao_51, questao_52, questao_53, questao_54, questao_55, questao_56, questao_57, questao_58, questao_59, questao_6, questao_60, questao_61, questao_62, questao_63, questao_64, questao_65, questao_66, questao_67, questao_68, questao_7, questao_70, questao_71, questao_72, questao_73, questao_74, questao_75, questao_76, questao_77, questao_78, questao_79, questao_8, questao_80, questao_81, questao_82, questao_83, questao_84, questao_85, questao_86, questao_87, questao_88, questao_89, questao_9, questao_90, questao_91, questao_92, questao_93, questao_94, questao_95, questao_96, questao_97, questao_98, questao_99, data, questao_69) FROM stdin;
16	17	5	0	0	1	2	5	1	0	1	3	3	2	0	4	3	0	0	0	0	0	5	0	0	2	1	1	1	5	0	0	7	9	1	1	1	\N	3	4	1	9	2	4	0	1	1	\N	1	2	1	0	1	1	{3}	4	1	1	0	2	2	5	2	0	0	0	4	5	2	2	0	0	0	6	1	0	0	4	5	1	5	3	0	1	3	2	7	1	1	6	5	0	5	5	3	1	1	3	2	\N	\N	\N	\N	\N	\N	{}	\N	\N	5	0	4	6	0	0	1	3	8	6	0	3	0	7	0	0	0	0	2	0	0	3	0	0	0	0	0	0	0	1	\N	\N	\N	\N	\N	2	0	0	0	2018-09-13	4
17	18	4	0	1	2	1	6	1	0	2	3	1	3	1	2	3	1	3	0	0	1	0	0	3	1	0	1	1	0	0	0	0	9	0	1	1	\N	2	0	1	2	2	\N	0	0	1	\N	1	2	0	1	1	1	{6}	3	1	1	1	0	2	4	0	0	3	0	0	0	4	4	1	0	4	5	2	0	0	4	5	1	4	2	0	4	4	0	5	2	0	2	1	0	2	2	2	1	1	2	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	2	0	5	2	0	1	2	2	1	\N	\N	\N	\N	\N	\N	0	2	0	0	6	0	0	0	0	1	4	0	1	\N	\N	\N	\N	0	0	2	1	1	2018-11-13	0
18	20	3	1	2	3	1	2	0	0	2	3	2	3	0	1	3	2	1	0	0	3	5	2	0	3	0	1	1	0	7	0	2	1	1	1	0	\N	1	1	1	5	0	2	0	1	1	1	1	2	0	1	1	1	{4}	6	0	0	1	0	2	0	0	0	0	0	3	3	1	3	3	0	2	7	3	2	0	6	1	1	5	5	0	2	2	3	6	1	6	3	6	0	2	4	6	2	1	1	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	6	2	3	0	2	0	0	2	1	0	5	0	0	0	1	6	0	1	0	0	5	1	2	1	1	0	3	0	1	\N	\N	\N	\N	\N	0	3	0	2	2018-09-13	2
19	19	5	1	0	0	0	6	1	0	0	0	1	1	1	0	0	0	0	1	2	3	5	4	4	0	0	0	0	7	7	7	4	6	0	0	0	1	0	1	1	10	2	6	1	0	0	1	0	2	2	0	0	1	{0}	4	0	1	1	5	4	4	4	0	4	2	8	8	2	8	8	0	8	5	0	8	5	8	2	1	5	8	1	8	0	0	8	7	0	0	0	1	8	9	8	2	1	3	3	0	\N	6	0	5	1	{1,2,3}	0	8	0	0	6	7	7	6	1	4	4	2	1	\N	\N	\N	\N	0	0	1	0	0	0	7	1	0	0	0	0	4	0	\N	6	0	0	0	1	0	3	0	0	2018-11-13	7
5	7	1	1	0	4	0	6	1	0	1	3	4	4	0	4	5	2	3	1	1	5	5	0	0	1	0	1	1	0	0	0	0	9	0	1	0	5	1	0	1	10	2	0	0	0	1	0	0	0	2	1	1	1	{4}	7	1	1	0	4	0	0	4	0	0	0	1	0	1	1	1	0	0	1	2	0	0	6	0	0	2	2	1	2	0	0	5	5	0	1	0	1	1	4	1	0	0	7	1	0	4	0	0	12	1	{2}	1	13	5	0	2	1	6	0	0	2	1	3	1	\N	\N	\N	\N	1	0	1	2	4	0	5	0	0	0	0	0	2	1	1	\N	0	\N	\N	\N	\N	1	0	1	2018-11-13	1
2	3	3	0	1	3	0	6	0	1	1	3	4	4	1	4	4	1	2	0	0	5	0	1	0	1	0	1	1	0	0	0	5	3	1	1	1	\N	2	1	0	5	0	6	0	0	0	\N	1	1	2	1	1	1	{6}	6	1	\N	1	0	0	0	0	0	0	0	3	3	1	3	1	0	1	3	3	1	0	6	1	1	5	2	0	1	0	1	3	2	3	6	6	1	6	5	3	1	1	3	1	0	4	0	0	13	1	{2,3}	1	\N	0	\N	3	5	2	6	0	3	3	1	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	\N	\N	0	0	0	2	0	1	\N	\N	\N	\N	0	0	4	2	3	2018-11-13	5
1	2	3	1	2	2	2	6	0	0	3	2	4	4	1	3	4	2	\N	0	0	5	5	1	1	1	0	1	1	2	1	0	6	9	0	1	1	\N	\N	1	0	0	0	4	0	0	2	\N	2	3	3	0	0	1	{6}	5	1	\N	0	4	2	3	0	1	0	0	6	6	6	3	3	0	3	7	1	1	1	6	1	0	6	1	1	3	1	1	3	1	5	6	\N	\N	\N	3	\N	\N	1	3	3	0	5	\N	0	13	1	{1,2,3}	1	\N	5	0	3	6	2	5	0	3	4	2	0	7	1	7	0	2	6	0	0	0	0	5	2	6	1	1	1	3	0	1	\N	\N	\N	\N	3	0	3	0	1	2018-11-13	2
10	11	5	0	0	4	2	\N	1	0	1	3	4	4	1	3	4	2	0	0	0	5	0	0	0	\N	0	1	1	1	0	0	0	\N	0	1	1	\N	2	1	0	0	0	12	0	0	2	\N	0	1	0	1	1	1	{2,7}	\N	1	1	0	0	4	0	0	0	0	1	5	6	0	1	0	0	1	1	2	0	1	6	1	1	2	3	1	1	1	1	6	3	3	5	6	0	1	3	3	1	1	5	3	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	5	0	\N	1	1	3	2	1	\N	\N	\N	\N	\N	0	1	1	0	0	7	0	0	0	0	0	2	1	1	0	0	0	0	0	0	4	1	0	2018-11-13	\N
11	12	5	1	0	3	1	6	1	0	0	3	3	4	0	2	5	0	2	0	0	4	5	0	0	2	0	1	1	0	0	0	0	\N	1	1	1	\N	0	2	1	\N	2	\N	0	1	0	\N	1	1	0	1	1	1	{6}	4	1	1	\N	0	0	0	0	0	0	0	6	6	0	0	1	0	2	3	4	0	0	6	1	0	5	5	1	2	2	1	8	2	0	5	5	5	6	2	5	1	1	3	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	7	3	6	0	4	2	6	1	\N	\N	\N	\N	0	0	1	0	0	1	\N	0	\N	\N	\N	\N	\N	0	1	\N	0	\N	\N	\N	0	1	1	2	2018-11-13	5
12	13	3	0	0	4	2	6	1	0	2	3	4	4	1	4	4	0	3	0	0	5	5	0	0	1	7	1	1	0	0	0	0	\N	\N	\N	1	\N	1	1	0	1	0	6	0	0	0	\N	1	2	1	1	1	1	{4}	4	1	\N	\N	0	2	0	1	0	0	0	1	3	3	7	3	0	3	3	3	3	1	3	1	2	1	1	0	1	3	1	3	3	7	2	4	2	4	2	3	2	5	1	5	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	0	0	0	3	0	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	0	4	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	0	4	4	4	2018-11-12	2
13	15	4	0	0	3	4	3	0	0	4	3	4	4	0	4	4	1	0	0	0	5	5	4	4	1	0	1	1	7	7	7	0	8	1	1	1	\N	0	4	\N	9	0	6	0	0	0	\N	1	1	0	0	1	1	{6}	6	1	1	1	0	0	5	0	0	0	0	5	5	0	1	3	0	2	6	6	3	0	5	5	5	5	5	0	2	5	0	7	1	3	5	5	1	5	3	5	1	3	0	4	0	3	9	1	\N	0	{}	0	13	0	4	4	7	5	6	0	4	3	8	0	6	0	0	0	1	\N	0	0	0	0	0	3	4	4	1	0	2	0	1	\N	0	0	0	0	0	1	0	4	2018-11-13	7
14	16	2	1	2	1	0	\N	1	1	3	3	4	3	1	3	2	0	2	0	0	3	5	0	3	2	0	1	1	1	0	0	0	\N	0	1	1	\N	4	4	0	5	0	4	0	0	1	\N	4	0	2	1	1	1	{4}	2	1	1	1	0	2	0	0	0	1	2	0	0	0	\N	\N	0	\N	\N	\N	0	0	6	0	0	0	1	0	5	0	0	3	0	0	1	6	0	0	3	0	1	0	6	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	0	\N	0	1	2	8	1	\N	\N	\N	\N	\N	6	1	4	0	0	7	0	0	0	0	0	3	0	1	\N	0	0	0	1	0	1	2	0	2018-11-13	0
15	14	1	0	1	3	0	\N	1	3	3	2	4	4	0	3	4	2	0	0	0	2	0	0	3	1	0	1	0	0	0	0	0	8	1	1	1	\N	2	4	0	0	0	4	0	0	1	1	1	2	0	1	1	1	{5}	4	1	1	1	0	2	0	4	0	0	2	6	6	2	3	6	0	7	6	3	5	6	6	1	3	7	8	1	3	4	0	5	5	0	4	6	5	7	3	8	0	5	6	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	0	0	0	0	1	4	8	1	\N	\N	\N	\N	1	0	1	0	0	0	3	0	0	1	0	0	3	0	1	\N	\N	\N	\N	\N	4	3	2	2	2018-11-13	0
50	23	5	0	3	1	2	6	0	1	0	3	4	4	0	4	4	1	3	1	0	5	5	1	0	2	0	1	1	0	1	0	0	9	1	1	1	5	2	1	0	0	0	6	0	0	1	\N	0	2	0	1	1	1	{2}	7	0	1	1	0	2	0	0	0	3	0	3	6	5	0	0	0	2	6	3	0	0	6	0	1	6	6	0	1	1	1	1	6	6	6	7	7	7	3	2	1	1	4	5	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	6	3	6	1	3	3	2	\N	\N	\N	\N	\N	0	0	1	3	0	1	\N	0	\N	\N	\N	\N	\N	0	\N	\N	0	0	0	5	0	4	3	2	2018-11-13	3
51	22	4	0	0	1	0	\N	1	1	0	3	0	4	1	2	3	1	2	0	0	5	0	0	0	1	0	0	1	0	0	0	0	7	1	1	1	\N	0	0	1	9	2	12	0	0	2	\N	2	2	1	1	1	\N	{6}	5	1	1	1	0	0	0	0	0	0	0	5	5	0	5	1	1	1	5	3	1	1	6	0	0	5	5	0	1	0	0	5	0	0	3	5	0	5	2	1	0	1	3	1	0	5	2	0	\N	1	{}	0	\N	0	2	2	7	0	0	1	2	2	0	0	6	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	5	0	1	\N	\N	\N	\N	\N	0	4	0	0	2018-11-13	0
4	6	4	0	1	3	2	2	1	0	2	3	4	4	1	4	5	1	3	0	0	5	0	1	4	4	0	1	1	0	0	0	\N	\N	0	1	1	\N	1	4	0	1	0	\N	0	0	0	1	1	2	1	1	1	1	{0,3,4}	6	0	1	1	4	2	4	\N	0	3	0	0	0	0	4	3	0	0	3	1	0	0	4	1	0	1	0	0	1	0	0	0	3	6	6	5	0	0	3	4	0	0	0	1	0	5	9	1	\N	1	{1,2,3}	1	\N	0	1	2	7	5	6	0	4	2	3	1	\N	\N	\N	\N	0	0	0	\N	\N	0	4	\N	\N	\N	0	4	3	0	0	\N	\N	\N	\N	\N	0	3	0	0	2018-11-13	5
7	10	5	0	0	2	1	6	0	0	1	2	3	3	0	1	3	2	0	0	0	0	5	0	0	3	0	1	1	0	1	0	0	\N	0	1	1	\N	2	1	0	0	0	4	0	1	2	\N	3	1	2	1	1	1	{6}	7	1	1	1	0	4	4	2	0	0	1	5	1	1	1	1	0	1	2	3	0	0	7	0	0	1	1	0	0	0	1	3	1	1	6	5	0	1	3	1	0	0	1	0	0	4	0	0	13	1	{2,3}	0	12	0	\N	2	0	0	\N	0	1	3	2	1	\N	\N	\N	\N	\N	0	1	0	0	0	1	0	0	0	0	0	0	0	1	\N	0	\N	\N	\N	0	3	0	1	2018-11-13	\N
8	8	5	0	0	1	1	6	1	0	2	2	4	4	0	3	4	1	3	0	0	5	5	0	0	2	0	1	1	0	0	0	0	\N	0	0	1	\N	2	1	0	7	2	\N	0	1	2	\N	3	2	0	0	0	1	{2}	6	1	\N	1	0	0	4	4	0	0	2	6	4	1	3	1	0	1	1	4	0	0	4	3	1	4	2	0	1	1	0	6	1	1	5	3	0	1	4	1	0	0	0	1	0	5	9	1	\N	1	{1,2,3}	0	12	0	\N	0	0	5	4	0	3	0	1	1	\N	\N	\N	\N	0	0	0	0	0	0	6	0	0	0	0	0	3	0	1	\N	0	0	0	5	0	3	0	0	2018-11-13	2
9	9	4	\N	1	0	0	3	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	0	0	0	7	7	7	0	8	1	0	0	5	0	0	0	4	0	2	0	1	0	0	0	2	1	0	1	0	{7}	6	0	0	1	0	2	5	0	1	0	0	6	5	7	\N	6	0	3	8	5	7	6	6	1	2	6	2	1	7	7	6	6	5	6	7	7	5	5	1	3	8	6	5	4	0	5	4	1	\N	0	{3}	0	13	0	0	6	7	7	2	0	4	9	8	0	4	0	0	0	2	6	0	3	0	0	0	4	6	0	2	0	4	0	0	6	0	0	0	4	0	4	1	2	2018-11-13	0
52	21	5	0	1	0	2	6	0	0	2	3	1	4	1	2	\N	2	2	0	0	5	1	4	0	4	0	1	1	5	7	5	0	2	0	1	1	\N	1	0	0	5	0	6	0	0	0	1	1	2	2	1	1	1	{7}	4	0	1	1	5	4	4	0	0	3	2	0	4	4	4	4	1	4	8	4	5	2	4	4	3	4	4	1	4	4	6	7	6	4	6	7	5	6	1	8	7	5	8	4	0	\N	\N	\N	\N	1	{}	\N	\N	0	4	7	7	5	4	1	4	9	5	0	5	0	0	0	1	0	0	1	4	0	5	0	0	0	2	0	2	0	0	5	0	0	0	0	0	4	1	1	2018-11-13	2
53	54	3	0	0	4	0	6	1	0	0	3	4	4	1	4	5	2	1	0	0	5	5	0	0	1	0	1	1	0	0	0	0	0	0	1	0	\N	0	0	1	10	2	12	1	0	0	1	0	2	0	1	0	1	{7}	1	0	1	1	\N	2	\N	\N	\N	\N	\N	0	0	8	6	0	0	8	8	2	6	0	8	4	1	4	7	1	8	3	5	0	0	0	8	4	2	6	6	8	8	8	4	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	4	2	2	1	2	9	8	0	4	0	0	0	0	0	1	0	1	0	3	0	0	0	4	0	4	0	1	\N	\N	\N	\N	\N	\N	2	0	0	2004-03-05	5
54	55	4	0	1	2	1	6	1	0	3	3	4	4	0	4	2	1	0	0	0	5	0	0	4	2	1	1	1	0	0	0	0	0	0	1	1	\N	2	0	0	0	0	6	0	0	1	\N	1	2	0	1	1	1	{2}	4	1	1	1	4	2	0	0	0	0	0	1	6	1	1	1	0	1	1	1	1	0	7	2	2	5	3	1	1	1	4	6	1	0	5	5	1	5	8	5	1	1	4	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	4	7	5	6	0	2	0	\N	1	\N	0	0	0	0	0	0	4	2	0	5	0	0	0	0	0	2	0	1	\N	0	0	0	5	0	3	1	1	2018-11-13	2
55	57	4	0	0	3	0	\N	1	0	0	1	4	4	1	4	4	1	3	0	0	5	5	0	0	1	0	1	1	0	0	0	0	0	0	1	1	\N	2	4	0	7	0	12	0	0	0	\N	1	2	2	1	1	1	{0}	7	1	1	1	0	0	0	5	0	0	0	5	5	5	0	3	0	3	6	0	1	0	5	3	1	0	4	1	5	3	0	7	0	4	0	6	1	6	3	0	1	3	6	4	\N	\N	\N	\N	\N	1	{}	\N	\N	2	1	2	0	3	3	0	1	0	1	1	\N	\N	\N	\N	0	\N	0	0	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	0	4	4	3	2018-11-13	0
56	56	0	1	0	1	0	0	0	0	0	3	2	4	1	4	4	0	1	0	0	0	0	0	1	1	0	1	\N	2	0	0	0	8	1	1	0	\N	1	1	0	0	0	6	0	1	3	1	1	2	0	1	1	1	{2}	1	1	1	0	0	2	0	4	0	3	0	7	8	8	8	2	0	8	6	3	1	5	8	8	8	8	8	1	6	8	8	6	8	8	6	8	8	8	5	8	8	7	8	8	0	\N	6	1	\N	0	{1,2,3}	1	\N	6	5	4	4	5	3	1	4	9	8	1	\N	0	0	0	1	\N	1	0	0	1	\N	\N	0	0	0	0	0	0	1	\N	\N	0	0	0	0	3	1	4	2018-10-13	3
57	58	1	0	0	0	0	\N	1	0	0	3	4	1	0	1	5	2	3	0	0	3	4	1	0	1	0	1	1	0	0	0	0	8	1	1	0	\N	2	1	0	10	0	12	0	0	0	0	2	2	0	1	1	\N	{0}	6	1	1	1	4	2	4	3	1	3	0	0	0	0	0	0	0	1	0	3	0	0	5	1	0	2	2	0	3	3	0	0	1	1	1	0	0	6	6	3	1	1	2	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	7	0	6	0	1	3	1	0	5	0	0	0	0	0	1	0	0	0	4	0	0	0	0	0	3	0	0	4	0	0	0	3	0	3	1	4	2018-11-13	1
59	60	4	0	0	2	2	6	1	0	1	2	4	4	0	2	3	1	3	0	0	1	4	3	1	1	0	1	1	0	1	0	7	9	1	1	0	\N	2	4	0	0	0	4	0	0	0	1	4	3	1	1	1	0	{4}	7	1	1	1	4	2	0	0	0	3	0	2	1	0	5	1	0	3	5	1	2	3	5	5	3	4	4	\N	3	1	0	0	5	5	1	5	0	5	2	0	6	3	5	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	3	6	2	4	0	4	4	3	1	\N	\N	\N	\N	1	\N	0	0	0	0	3	0	2	7	0	0	2	0	1	\N	\N	\N	\N	1	\N	2	1	4	2018-11-13	0
60	63	4	0	1	3	1	\N	1	0	2	2	4	4	0	4	4	2	3	0	0	5	5	0	0	3	0	1	1	0	0	0	7	5	1	1	1	\N	0	0	0	9	0	6	0	0	2	\N	3	3	1	1	1	1	{6}	3	1	1	1	4	2	3	5	0	3	0	1	2	1	1	1	0	1	2	1	1	0	5	1	1	4	3	0	1	1	1	6	1	4	3	4	3	2	3	1	1	1	1	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	3	3	1	5	6	0	4	0	1	1	\N	\N	\N	\N	0	\N	1	1	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	0	3	1	0	2018-11-13	5
61	65	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	2	1	1	1	4	\N	5	5	0	3	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-13	\N
62	66	4	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	4	1	\N	1	0	2	0	0	0	3	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-13	\N
63	64	1	1	0	3	0	\N	1	0	1	1	4	4	1	2	3	1	0	0	0	4	5	0	1	1	0	1	1	0	0	0	0	8	0	1	1	\N	1	3	1	0	2	12	0	0	3	\N	0	2	0	1	1	1	{4}	2	1	1	1	0	2	0	0	0	3	0	2	2	2	2	0	0	1	2	0	0	0	6	0	0	1	0	1	3	0	0	0	0	1	0	3	0	0	3	1	1	4	0	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	0	0	0	1	1	6	2	1	6	\N	\N	\N	1	0	0	1	0	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	4	4	0	3	2018-11-13	0
3	4	3	1	0	4	0	6	0	0	1	3	4	4	0	3	4	0	1	0	0	5	5	0	0	1	0	1	1	0	0	0	0	\N	1	\N	1	\N	0	1	0	2	0	5	0	0	1	\N	1	2	2	1	1	1	{6,7}	4	0	0	1	3	0	3	0	0	0	0	5	2	0	1	0	0	1	3	3	0	0	3	1	1	1	0	0	2	1	2	3	4	4	6	6	0	2	3	0	1	0	1	0	0	0	0	0	13	1	{}	0	1	0	\N	2	5	5	3	0	2	0	2	1	\N	\N	\N	\N	\N	1	0	0	0	0	1	0	0	0	0	0	1	0	1	\N	\N	\N	\N	0	0	4	0	3	2018-11-13	0
6	5	3	1	0	1	1	2	1	0	\N	3	1	4	1	1	2	1	0	0	0	0	0	0	0	1	0	1	1	0	0	0	0	\N	2	1	1	\N	0	1	0	7	0	4	0	0	0	\N	1	2	1	1	1	1	{4}	3	1	1	\N	5	0	5	4	0	0	0	0	0	1	0	1	0	0	0	0	0	0	5	0	0	0	0	1	0	0	0	5	0	5	0	2	0	0	5	0	0	0	0	0	0	5	9	1	\N	1	{2,3}	0	12	5	2	2	7	0	6	1	2	0	\N	0	4	0	0	0	1	0	1	0	4	1	\N	\N	\N	\N	0	0	0	0	1	\N	\N	\N	\N	0	0	4	0	2	2018-11-13	2
67	70	4	1	0	3	1	3	0	0	0	3	4	4	1	4	3	0	3	0	0	5	5	0	0	1	0	1	1	0	0	0	0	9	0	1	1	\N	0	1	0	0	0	6	0	0	0	\N	1	3	1	1	1	\N	{4}	7	1	1	0	0	2	0	4	0	0	0	5	5	5	5	5	1	0	5	5	0	5	6	0	2	5	0	1	4	5	0	6	5	5	5	5	0	5	1	0	0	0	5	0	0	5	8	0	12	0	{1,2,3}	0	13	5	0	\N	7	1	6	0	1	\N	0	1	\N	\N	\N	\N	1	0	1	1	0	0	7	1	2	1	0	0	3	1	1	\N	0	0	0	1	0	2	2	1	2018-11-13	2
58	59	1	1	3	2	2	4	0	0	1	1	0	4	0	2	3	1	0	0	1	5	2	3	2	1	1	\N	1	4	2	0	0	1	2	1	1	2	0	4	1	3	2	7	1	1	0	\N	1	2	2	0	0	0	{3}	5	0	0	0	0	2	0	0	0	0	0	5	5	6	4	1	0	1	5	1	5	5	5	1	2	6	3	1	3	7	5	1	4	2	1	5	5	5	2	1	3	3	1	6	0	5	1	1	4	0	{1,3}	0	13	2	4	4	3	2	1	1	4	4	4	0	2	3	4	0	2	6	0	1	1	\N	11	4	3	8	2	3	3	0	0	2	2	0	1	2	0	1	4	2	2018-11-13	6
64	68	\N	1	0	0	0	\N	\N	0	3	0	3	3	1	0	5	1	1	0	0	0	0	0	0	2	0	1	1	1	0	0	0	9	2	0	1	2	3	0	0	0	2	6	0	1	3	\N	4	2	0	1	1	1	{2}	\N	1	1	0	5	2	5	0	0	3	2	2	2	1	1	1	0	0	1	1	6	6	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	4	0	0	0	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	4	1	4	0	0	0	1	0	0	0	1	0	0	0	0	0	0	1	0	0	0	6	1	3	4	0	0	3	1	1	\N	0	0	0	1	\N	2	0	0	2018-11-13	0
65	67	3	0	0	2	4	6	1	1	0	0	4	3	0	2	5	1	2	0	0	3	5	0	2	1	0	1	1	0	0	0	0	8	0	1	1	\N	2	0	0	0	0	12	0	0	3	\N	4	4	0	0	1	1	{0,3,4}	6	1	1	1	4	2	0	0	0	0	0	5	5	2	0	2	0	1	0	4	0	0	5	0	0	7	5	0	1	1	0	5	0	0	5	5	0	5	4	1	0	0	1	0	0	\N	\N	\N	\N	1	{}	\N	\N	5	0	3	0	0	\N	0	0	9	8	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	3	0	1	\N	\N	\N	\N	\N	0	4	\N	2	2018-11-13	0
66	69	4	1	1	3	2	6	1	0	2	3	4	4	0	3	3	0	1	0	0	1	5	0	0	1	0	0	1	0	0	0	0	8	2	1	1	\N	2	1	0	0	0	4	0	0	0	\N	0	2	0	1	1	1	{0}	4	1	1	1	5	2	0	4	0	0	0	1	1	5	2	1	0	1	3	3	1	1	6	\N	0	5	1	0	1	1	3	5	1	6	6	6	0	0	6	3	3	1	1	6	\N	\N	\N	\N	\N	0	{}	\N	\N	5	2	2	7	2	0	1	2	4	2	1	\N	\N	\N	\N	1	0	1	2	0	1	\N	0	\N	\N	\N	\N	\N	1	\N	\N	0	0	0	0	0	4	1	0	2018-11-13	0
68	72	4	1	1	1	2	0	1	0	2	3	4	4	1	4	2	1	0	0	0	0	0	0	0	1	0	1	1	0	2	0	1	5	0	1	1	\N	0	0	0	0	0	\N	0	1	0	1	0	2	0	1	1	1	{5}	5	1	1	1	1	0	0	2	0	3	0	3	1	0	1	1	0	1	7	0	3	4	1	3	1	3	1	1	0	1	0	3	3	2	3	4	2	4	2	0	0	1	2	4	0	5	1	1	\N	1	{2,3}	0	5	5	0	2	2	2	5	0	3	7	2	1	\N	\N	\N	\N	0	0	1	0	0	0	8	0	0	0	0	1	2	0	1	\N	\N	\N	\N	\N	\N	1	4	1	2018-11-13	1
69	71	2	1	0	1	2	4	1	0	0	3	4	0	0	4	5	0	3	0	0	2	4	4	2	1	2	1	1	2	6	4	0	1	1	1	1	\N	2	4	0	0	0	0	0	0	0	1	0	0	0	0	0	0	{4}	5	1	0	1	0	2	0	0	0	1	1	1	8	1	3	2	0	8	8	1	2	1	8	0	3	7	7	1	2	2	1	8	4	8	2	8	0	8	5	6	2	1	8	6	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	3	7	0	0	0	2	9	0	0	6	0	7	0	0	0	1	0	0	1	7	0	0	7	0	0	4	1	1	\N	0	0	0	0	1	4	1	0	2018-11-13	5
70	73	3	0	0	1	4	6	1	1	1	0	4	4	1	2	5	1	0	0	0	0	5	0	0	1	0	1	1	0	0	0	0	\N	0	1	1	\N	1	2	1	5	0	\N	0	0	0	\N	0	2	0	1	1	1	{4}	5	1	1	0	4	2	0	0	0	0	0	0	0	0	0	2	0	1	6	4	0	0	8	0	2	3	5	1	1	2	3	5	0	0	5	3	0	0	2	2	2	0	2	0	0	5	2	1	\N	1	{2}	1	\N	5	0	3	0	0	\N	0	0	9	8	1	\N	\N	\N	\N	0	0	0	0	0	0	7	1	2	1	0	0	3	0	1	\N	\N	\N	\N	\N	0	3	0	3	2003-12-20	0
71	74	4	1	1	3	2	6	1	0	2	3	4	4	1	3	3	1	0	0	0	3	5	0	0	1	0	1	1	0	0	0	0	8	1	1	1	\N	2	1	0	5	0	12	0	0	1	\N	1	2	0	1	1	1	{0}	6	1	1	0	0	2	0	4	0	0	1	1	1	3	1	1	0	1	3	2	2	1	5	0	0	2	1	1	1	0	0	5	1	3	2	5	0	1	1	1	0	0	1	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	0	5	1	0	3	2	3	1	\N	\N	\N	\N	1	0	0	0	0	1	\N	0	\N	\N	0	0	0	0	1	\N	\N	\N	\N	\N	0	4	0	2	2018-11-13	1
72	76	4	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	4	1	1	1	0	2	1	0	0	3	0	5	6	8	5	5	0	4	8	5	5	6	7	1	3	5	1	1	4	5	1	8	0	8	6	7	6	5	5	8	5	6	5	5	0	5	7	0	11	1	{1,3}	0	13	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2003-07-21	\N
73	75	4	0	2	2	3	2	0	0	2	3	3	4	0	2	2	1	0	0	0	5	5	3	2	1	0	1	1	6	0	0	0	5	0	1	1	\N	2	2	1	9	0	2	0	0	3	\N	4	3	1	1	1	1	{4}	4	1	1	1	2	2	3	3	0	0	0	3	3	2	2	2	0	1	6	3	1	0	5	2	2	0	3	1	3	1	0	7	1	0	0	2	0	2	1	3	1	2	7	1	0	4	0	0	3	1	{2}	0	6	5	1	2	2	1	0	0	2	5	5	0	7	0	0	1	0	1	1	2	2	0	5	3	6	8	3	0	3	0	0	8	1	1	2	0	2	2	1	1	2018-11-13	2
74	79	4	1	1	3	1	6	0	0	0	3	4	4	0	3	3	1	3	1	0	5	5	4	4	2	7	0	0	0	4	2	1	0	0	1	1	\N	0	1	0	0	1	4	1	1	0	\N	1	2	1	1	1	1	{0}	6	1	1	1	0	2	0	0	0	0	0	5	5	3	3	2	0	7	6	6	5	2	7	5	4	6	5	1	3	2	2	6	2	8	7	6	2	4	1	3	1	1	3	4	\N	\N	\N	\N	\N	1	{}	\N	\N	1	0	4	0	5	6	0	4	6	7	0	5	0	0	0	0	0	0	0	2	0	1	4	3	1	4	0	1	0	0	4	0	0	0	2	\N	0	2	2	2018-11-13	5
75	78	4	1	1	3	2	6	1	0	2	3	4	4	0	2	3	1	1	0	0	3	5	0	0	2	0	1	1	0	0	0	0	1	0	1	1	\N	2	1	0	0	0	4	0	0	0	\N	0	2	0	1	1	1	{0}	\N	1	1	0	0	2	0	4	0	0	1	1	1	1	1	1	0	1	3	3	1	1	6	0	1	1	1	0	1	1	1	5	0	1	5	5	1	1	3	1	1	0	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	2	0	1	1	0	1	2	3	1	\N	\N	\N	\N	1	0	0	0	0	1	\N	1	\N	\N	\N	\N	\N	1	\N	\N	0	0	0	0	0	4	0	1	2018-11-13	1
76	77	5	1	3	4	0	\N	1	0	2	3	4	3	1	2	3	0	0	0	0	0	0	0	0	1	0	1	0	1	0	0	0	\N	0	1	1	\N	2	1	1	\N	2	\N	0	0	0	\N	2	2	0	1	1	1	{4}	7	1	1	0	0	2	0	4	0	0	0	1	1	5	\N	\N	0	\N	\N	2	\N	\N	6	\N	0	1	\N	0	\N	\N	\N	2	0	1	6	0	\N	\N	5	2	\N	\N	0	0	\N	\N	\N	\N	\N	0	{}	\N	\N	1	\N	2	1	0	5	1	1	2	1	1	\N	\N	\N	\N	1	\N	0	0	0	0	8	0	0	0	0	0	2	0	1	\N	\N	\N	\N	0	0	2	0	3	2018-11-13	0
77	80	1	0	1	0	3	6	0	1	3	1	3	3	0	2	4	0	0	0	0	2	4	0	1	1	0	1	1	0	1	0	0	8	2	1	1	\N	1	1	1	9	0	6	0	0	0	1	0	1	1	1	0	1	{0}	7	1	1	1	4	2	0	4	0	0	2	1	1	0	0	0	1	1	1	1	0	0	4	1	0	4	1	1	1	1	0	1	1	2	4	1	0	4	5	1	1	1	4	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	2	3	3	2	6	0	4	3	8	1	\N	\N	\N	0	0	\N	0	0	0	0	4	0	0	0	0	0	1	0	\N	\N	0	0	0	0	0	1	0	2	2018-11-13	2
78	81	4	1	2	1	1	6	1	1	0	3	4	4	0	4	3	1	3	0	0	0	5	0	0	1	0	1	1	0	0	0	0	\N	1	1	1	\N	1	0	0	0	0	12	0	0	0	\N	0	2	3	1	1	1	{0}	7	1	1	\N	0	2	0	0	0	3	0	5	0	1	1	1	0	1	1	1	1	1	6	0	0	1	1	0	1	0	1	1	1	4	6	5	0	5	4	1	1	0	1	1	0	5	0	\N	\N	1	{3}	0	\N	5	0	2	7	5	6	0	1	4	1	1	\N	\N	\N	\N	1	0	0	\N	\N	1	\N	\N	\N	\N	0	0	5	0	1	\N	\N	\N	\N	\N	\N	4	1	0	2004-01-24	2
79	83	\N	0	0	0	0	\N	1	0	1	2	4	4	0	4	4	1	0	0	0	3	4	0	0	2	0	1	1	0	0	0	0	8	0	1	1	\N	2	0	0	0	0	\N	0	0	2	\N	4	0	2	1	1	0	{4,6}	5	1	1	1	4	2	0	0	0	\N	0	0	3	1	1	1	0	1	5	0	0	0	4	2	3	5	8	0	2	3	0	3	5	2	3	5	6	3	5	5	1	1	0	1	0	5	1	\N	1	1	{2}	\N	\N	0	2	4	6	4	5	0	2	2	1	1	\N	\N	\N	\N	1	8	0	0	0	1	\N	0	\N	\N	\N	\N	\N	0	\N	\N	0	0	0	1	0	4	2	4	2018-11-13	4
80	82	4	0	1	3	0	\N	0	1	1	3	4	3	0	3	4	1	2	0	0	5	5	3	1	1	0	1	1	0	0	0	0	\N	0	1	1	\N	2	1	1	1	2	\N	0	0	2	\N	3	1	1	1	1	1	{3}	7	1	1	1	0	2	0	4	0	0	0	5	6	5	6	1	1	3	3	5	1	5	5	1	1	5	5	1	7	5	5	5	3	3	6	7	6	8	1	6	1	1	8	3	0	3	1	0	8	0	{1,2}	1	\N	5	0	2	0	1	0	0	1	9	2	0	5	0	0	0	1	0	0	2	1	0	5	1	5	1	1	0	2	0	\N	\N	\N	\N	\N	\N	0	3	2	2	2018-11-13	0
81	85	3	0	2	3	1	6	0	0	0	3	4	4	0	3	3	1	3	2	0	3	4	1	1	3	0	1	1	2	0	0	0	9	1	1	1	\N	1	2	0	0	1	4	0	1	1	1	1	1	2	1	1	1	{4}	1	1	1	1	0	2	2	2	0	0	0	1	1	1	1	3	0	0	2	0	2	0	3	0	1	4	3	0	3	0	1	4	5	6	6	5	3	6	3	2	1	0	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	6	0	2	3	4	5	0	3	3	3	0	6	0	0	0	1	0	1	0	0	0	6	0	0	0	1	0	1	0	1	\N	\N	0	0	1	1	2	1	0	2018-11-13	4
82	84	3	0	1	4	1	6	1	0	0	3	3	4	0	4	3	2	0	0	0	4	5	2	2	1	0	1	1	0	1	1	0	9	1	1	1	5	0	1	1	0	0	6	0	0	0	\N	0	1	0	1	1	1	{4}	1	1	1	0	0	3	0	0	0	0	1	5	4	0	5	0	0	1	6	6	0	2	3	6	1	6	2	0	3	0	0	4	0	3	6	5	0	6	3	2	2	2	2	0	0	\N	1	0	1	1	{2}	0	6	6	0	2	7	7	6	0	4	3	1	0	2	0	0	0	0	0	1	0	0	0	1	0	0	0	0	0	2	0	1	\N	\N	\N	\N	0	0	4	4	1	2018-11-13	0
83	87	0	0	2	2	2	\N	1	1	\N	3	\N	2	0	2	4	0	1	1	2	5	5	1	0	1	0	1	1	\N	0	0	0	\N	0	1	1	5	0	1	0	1	0	12	1	1	0	\N	0	2	0	0	0	0	{4}	\N	0	0	1	0	0	0	0	0	0	2	1	0	1	0	1	0	0	4	1	0	0	1	0	1	0	1	0	1	0	1	1	1	1	1	1	1	3	\N	1	2	5	0	1	\N	\N	\N	\N	\N	1	{}	\N	\N	1	0	2	7	1	6	0	2	2	0	1	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	1	0	2	0	2018-11-13	1
84	86	4	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	7	0	0	1	0	\N	0	0	0	0	0	6	6	6	0	0	0	0	5	5	5	1	5	2	2	5	1	1	5	1	1	5	0	5	5	\N	\N	\N	7	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	5	6	4	5	0	3	9	8	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-13	2
85	89	5	0	0	4	2	3	1	0	0	3	4	4	0	4	4	1	3	0	0	5	5	4	0	2	0	0	0	0	0	0	0	8	1	1	1	\N	0	0	0	2	0	6	0	0	0	\N	2	3	0	1	1	1	{1,2,4,5,6,7}	6	1	1	1	0	4	0	0	0	3	0	6	6	3	3	3	0	3	6	5	3	4	6	6	3	4	3	0	3	3	4	6	4	5	6	5	5	6	3	3	2	3	5	3	0	5	8	0	13	0	{2,3}	1	\N	0	\N	2	7	5	6	1	4	3	3	1	6	0	0	0	0	0	0	0	0	0	3	0	0	0	1	0	1	0	1	\N	0	0	0	0	0	4	4	3	2018-11-13	5
86	88	4	1	0	4	1	\N	1	0	4	3	3	4	0	4	4	2	1	0	0	5	5	0	0	1	0	1	1	0	0	0	0	9	1	1	1	\N	1	0	0	0	0	6	0	0	1	\N	0	2	3	1	1	1	{4}	7	0	0	0	0	0	0	4	2	0	0	5	2	0	5	0	0	0	0	6	5	5	5	5	0	5	0	0	1	2	0	5	3	3	3	5	5	5	5	6	1	1	0	0	0	5	6	0	\N	1	{2}	1	\N	0	0	2	7	5	6	0	4	0	1	1	\N	\N	\N	\N	0	0	1	0	0	1	\N	0	0	0	0	0	2	0	1	\N	\N	\N	\N	0	0	4	3	2	2018-11-13	1
87	91	3	1	1	3	2	0	1	0	2	2	4	4	0	4	5	1	2	0	1	3	5	0	1	2	1	1	0	0	2	0	0	\N	1	1	1	\N	2	1	0	1	0	4	0	0	1	\N	2	0	0	0	1	1	{4}	1	1	1	0	4	2	4	3	0	3	0	5	5	5	0	0	0	2	2	5	0	0	2	5	2	5	5	1	5	2	0	2	0	0	0	5	2	5	4	2	2	2	5	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	2	3	6	4	5	0	3	4	0	0	7	0	0	0	0	6	0	3	1	0	6	1	1	7	0	1	3	1	1	\N	0	0	0	1	1	2	1	2	2018-11-13	4
88	90	4	0	2	2	1	3	1	1	2	2	2	3	0	1	2	2	0	0	0	2	5	0	2	3	1	1	1	2	0	1	0	8	0	1	1	\N	2	0	1	\N	2	\N	0	0	1	1	3	3	0	1	1	1	{0}	4	1	0	1	2	2	2	3	0	0	0	0	0	1	2	0	0	1	3	1	0	0	6	1	2	2	3	\N	5	1	0	5	1	5	5	5	0	1	6	5	0	3	3	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	2	0	0	0	0	1	1	3	0	4	0	3	0	1	9	1	2	2	0	4	2	6	8	2	1	3	0	0	7	1	0	0	2	1	2	0	0	2018-11-13	0
89	92	4	0	0	1	1	6	1	0	1	2	3	3	0	3	5	1	3	0	0	2	3	4	0	1	0	1	1	0	0	0	0	9	0	1	1	\N	4	4	0	7	0	4	0	0	3	\N	4	4	0	0	0	1	{7}	1	1	1	1	4	2	5	5	0	0	0	0	0	0	8	2	1	0	1	0	0	0	0	0	0	1	1	1	2	0	0	4	2	1	0	2	0	2	2	1	0	0	0	4	\N	\N	\N	\N	\N	1	{}	\N	\N	4	0	\N	\N	\N	\N	0	0	0	3	0	7	\N	\N	\N	\N	\N	1	\N	\N	0	7	0	0	0	4	4	3	0	1	\N	\N	\N	\N	\N	0	1	2	0	2018-11-12	\N
90	93	3	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	3	1	\N	0	0	0	0	0	0	0	0	1	3	3	1	0	0	0	0	1	0	0	6	0	0	0	0	1	6	0	0	5	1	1	6	5	0	1	4	2	0	1	3	1	0	1	0	0	13	1	{1,2,3}	0	6	0	6	\N	\N	2	0	0	1	5	7	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-13	2
91	94	4	1	0	3	0	\N	1	0	0	3	4	4	1	2	5	1	0	0	0	4	5	0	0	1	0	1	1	0	0	0	0	\N	0	1	1	\N	2	0	1	\N	\N	\N	0	1	0	\N	1	2	0	1	1	1	{3}	1	0	0	0	0	2	0	0	0	0	0	4	4	0	0	2	0	1	1	0	1	1	6	2	2	6	6	1	4	0	1	1	1	1	1	4	4	4	9	1	0	5	5	5	0	5	1	0	7	1	{0}	0	13	0	\N	0	7	3	6	0	4	4	6	0	2	0	0	0	0	0	1	0	2	0	1	0	0	0	3	0	1	0	1	\N	0	0	0	0	1	4	1	3	2018-11-13	5
92	101	1	1	1	3	2	0	0	3	3	3	3	3	1	4	3	1	1	0	0	5	0	0	0	1	0	1	0	5	7	0	1	0	2	1	1	\N	0	2	0	5	2	\N	0	0	2	\N	0	2	0	1	1	1	{0,3,4,5}	4	1	1	0	0	3	0	4	0	0	0	0	0	0	0	0	0	0	1	2	0	0	6	0	0	2	2	0	3	1	0	3	1	1	3	6	1	1	4	4	0	0	3	1	0	5	8	0	11	1	{1,2,3}	0	12	7	1	2	5	2	6	1	4	1	8	1	\N	0	\N	\N	0	0	1	0	0	0	4	0	0	0	0	0	3	0	1	\N	\N	\N	\N	3	0	4	4	\N	2018-11-06	7
93	102	4	0	0	2	2	6	1	0	1	3	\N	1	0	4	5	2	0	0	0	5	5	1	0	1	0	1	1	0	0	0	0	8	2	1	1	\N	2	1	1	\N	2	\N	0	0	2	\N	2	0	2	1	1	1	{3}	6	0	0	1	4	2	0	0	0	0	0	0	0	1	0	0	0	0	0	1	0	0	0	0	0	2	2	0	0	0	0	4	1	3	5	4	0	4	3	3	0	0	3	0	0	0	0	0	11	1	{2,3}	1	\N	7	1	2	5	1	1	1	2	9	8	1	\N	\N	\N	\N	0	0	0	3	0	0	4	0	0	0	0	0	1	0	1	\N	\N	\N	\N	0	0	3	0	2	2018-11-06	0
94	103	2	1	0	3	0	\N	1	0	3	2	1	4	1	1	1	0	1	3	0	0	0	0	0	1	0	1	1	1	1	0	0	9	1	1	1	\N	4	4	0	6	0	4	0	0	3	\N	3	2	0	1	1	1	{0,5}	6	0	1	1	4	2	3	5	0	0	0	0	2	1	1	0	0	6	4	3	2	0	4	1	0	3	2	0	3	6	6	8	5	1	1	3	0	2	6	0	1	1	8	1	0	5	0	0	13	1	{1,2}	1	2	5	0	2	1	0	3	0	2	0	0	1	\N	0	\N	\N	\N	\N	0	4	0	\N	7	0	0	0	1	0	3	0	1	\N	\N	\N	\N	0	0	3	0	0	2018-11-07	0
95	104	4	1	0	2	0	\N	1	0	2	3	2	4	0	4	3	1	2	0	0	0	5	0	0	1	0	1	1	0	0	0	0	\N	0	1	1	\N	1	1	0	0	0	4	0	0	0	\N	4	0	0	1	1	1	{4}	7	0	0	0	3	2	0	0	0	0	0	1	1	1	1	0	1	1	1	6	0	0	6	5	1	7	0	1	1	1	0	1	1	1	5	5	1	1	1	1	1	1	1	6	0	3	\N	0	\N	1	{2}	0	13	0	0	2	1	0	0	0	1	1	1	1	\N	\N	\N	\N	0	0	1	0	1	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	0	2	4	2	2018-11-07	0
96	105	4	1	2	2	1	6	1	1	3	2	2	4	1	4	3	0	1	0	0	4	5	0	0	1	0	1	1	0	0	0	0	\N	2	1	1	\N	1	1	1	9	0	12	0	0	0	\N	0	2	2	1	1	1	{0,3,4}	4	1	1	1	0	0	0	4	0	0	0	7	7	1	1	4	0	4	4	4	0	0	6	7	5	2	6	1	2	0	0	6	1	2	3	5	1	1	3	7	2	1	7	2	0	5	\N	\N	\N	1	{}	\N	\N	5	0	2	0	4	3	0	3	0	0	1	\N	\N	\N	\N	0	0	1	0	0	1	\N	\N	\N	\N	\N	\N	\N	1	1	\N	\N	\N	\N	\N	\N	4	4	2	2018-11-06	2
97	107	4	0	1	3	2	3	0	0	1	3	2	4	1	4	5	1	1	2	0	5	5	0	1	1	0	1	1	0	2	1	0	8	2	1	0	\N	0	1	0	1	0	4	0	0	0	0	1	1	2	1	1	1	{5}	1	1	1	1	0	2	0	0	0	0	0	2	1	0	1	0	0	2	2	0	0	0	1	1	1	0	2	0	1	2	0	3	1	3	4	2	1	4	3	3	1	1	4	1	0	5	0	\N	\N	1	{}	\N	\N	5	0	2	7	7	6	0	2	4	3	1	\N	0	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	0	1	1	\N	\N	\N	\N	\N	0	4	2	4	2018-11-06	7
98	106	3	1	2	3	1	6	1	0	1	3	3	4	0	4	3	2	1	0	0	0	5	1	0	1	0	1	1	0	1	0	\N	\N	0	1	1	\N	3	1	1	\N	2	0	0	0	2	\N	3	3	0	1	1	1	{3,4}	7	1	1	0	0	2	0	0	0	\N	0	5	1	1	2	0	0	1	2	0	2	0	6	2	2	6	2	0	1	2	5	5	0	2	6	7	1	5	3	2	0	3	8	2	\N	\N	\N	\N	\N	1	{}	\N	\N	7	0	2	5	0	0	1	1	9	1	1	\N	\N	\N	\N	1	0	1	4	1	0	7	0	0	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	0	2	0	2018-09-06	0
99	108	4	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	0	1	2	2	2	5	2	1	1	1	\N	0	2	\N	8	2	5	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	{3}	4	1	1	1	2	4	2	4	1	3	2	6	7	5	3	5	0	5	\N	6	5	\N	7	7	6	3	4	1	6	3	8	\N	0	4	7	3	3	3	3	3	2	2	5	2	\N	\N	\N	\N	\N	\N	{}	\N	\N	5	0	3	5	7	3	1	3	9	8	0	5	0	5	0	0	0	0	4	4	0	1	0	0	0	0	0	0	0	1	\N	\N	\N	\N	3	\N	\N	\N	\N	2018-11-06	7
100	109	4	0	2	2	1	6	0	0	1	3	2	4	0	4	5	2	0	0	0	3	0	0	0	2	0	1	0	0	0	0	1	2	1	1	1	\N	0	0	0	0	0	6	0	0	0	1	0	2	0	1	1	1	{2,5}	7	1	1	1	4	2	0	4	0	3	1	2	3	1	1	1	0	1	1	1	1	1	8	8	8	8	2	1	2	1	1	3	1	0	8	8	8	8	3	8	1	1	8	8	0	\N	2	0	13	1	{1,3}	0	1	5	0	2	2	0	4	0	2	7	6	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	0	0	0	0	0	2	0	1	\N	0	0	0	5	0	2	1	4	2018-11-06	2
101	112	3	0	2	1	4	4	0	0	3	1	\N	4	0	4	3	1	0	0	0	1	5	4	0	1	0	1	0	0	2	0	0	\N	1	0	1	0	4	2	0	0	0	0	0	0	0	\N	4	0	2	1	1	1	{0}	7	0	0	0	4	3	4	0	0	0	0	5	5	1	0	1	0	4	2	2	1	0	8	1	2	5	2	1	2	2	0	8	0	6	8	8	1	8	7	7	1	1	7	2	\N	\N	\N	\N	\N	1	{}	\N	\N	6	0	2	0	0	6	0	1	9	8	0	6	0	0	0	2	6	0	4	2	0	6	1	4	4	4	0	3	0	0	6	0	0	0	4	1	0	0	0	2018-11-06	0
102	110	4	1	0	2	2	6	1	0	2	3	4	4	0	4	3	2	2	0	0	5	5	4	0	1	0	1	1	0	0	0	0	\N	2	1	1	\N	1	1	1	\N	2	\N	0	0	0	\N	0	0	2	1	1	1	{4}	7	1	1	1	2	2	0	4	0	3	1	3	3	3	2	1	0	3	1	3	1	3	5	2	1	3	3	1	2	1	1	2	0	0	5	0	0	0	1	2	1	1	4	1	0	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	2	1	4	0	2	1	3	0	7	0	0	0	0	6	1	1	0	0	7	2	4	8	\N	0	3	0	1	\N	\N	\N	\N	\N	0	4	2	4	2018-11-06	1
103	111	4	0	2	4	2	2	0	0	2	3	4	4	1	4	3	0	3	0	0	5	0	0	0	2	0	1	\N	0	0	0	1	9	1	1	1	\N	2	0	0	2	0	2	0	0	0	\N	2	2	3	1	1	1	{0,2,4,6}	4	1	1	1	4	2	4	0	0	0	1	0	1	1	1	3	1	2	1	4	0	0	6	1	1	2	2	1	3	1	3	5	1	6	6	3	2	1	1	1	0	1	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	0	0	0	0	4	6	5	1	\N	\N	\N	\N	\N	\N	0	0	0	\N	\N	\N	\N	\N	0	0	1	0	1	\N	\N	\N	\N	5	0	1	1	0	2019-11-05	0
104	113	5	1	1	2	0	\N	1	0	2	2	1	4	0	4	5	1	1	0	0	0	5	1	0	1	0	1	1	0	0	0	\N	\N	0	1	1	\N	1	0	1	\N	\N	\N	0	1	1	\N	1	2	0	1	1	1	{6}	7	1	\N	1	3	2	5	0	0	1	0	3	0	0	1	0	0	0	0	1	0	0	4	0	0	1	0	1	0	0	0	2	0	2	1	3	0	3	2	0	0	1	0	0	\N	\N	\N	\N	\N	0	{}	\N	\N	5	1	2	0	0	\N	0	1	8	6	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	0	\N	\N	\N	0	4	0	0	2003-11-07	0
105	114	3	0	1	3	0	\N	1	1	0	2	4	3	0	4	5	1	2	0	0	5	5	4	1	1	0	1	0	0	0	0	0	\N	1	1	1	\N	1	0	1	0	0	4	0	0	1	\N	1	2	0	1	1	1	{4}	1	0	0	1	4	2	\N	3	0	0	0	0	0	1	0	0	0	0	3	0	0	0	3	0	1	3	0	0	4	0	0	1	4	0	6	2	0	6	2	3	0	1	2	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	2	2	0	1	2	3	1	\N	0	\N	\N	\N	\N	1	4	1	0	6	0	\N	\N	1	0	1	1	1	\N	\N	\N	\N	0	0	3	4	3	2018-11-07	0
108	118	1	1	2	1	3	6	0	0	3	2	4	4	0	4	3	2	0	0	0	0	5	0	1	1	0	1	0	0	1	1	7	2	1	1	1	\N	2	0	0	0	0	12	0	0	1	\N	1	2	0	1	1	0	{0}	4	1	1	1	0	2	0	4	0	0	0	1	5	5	1	0	0	2	8	6	1	0	6	2	2	5	2	1	6	6	1	8	2	3	6	8	0	3	3	3	2	2	3	2	1	2	\N	\N	\N	1	{}	\N	\N	5	1	2	0	1	1	0	2	9	8	0	6	0	0	0	2	6	1	4	4	0	5	0	0	0	1	0	1	0	0	6	0	0	0	2	1	2	1	2	2018-11-06	0
109	121	3	0	3	4	1	2	1	0	2	1	4	4	0	4	5	2	1	0	0	5	5	2	0	1	0	1	1	0	0	0	1	8	0	1	1	4	2	1	0	0	0	6	0	0	3	1	0	2	2	0	1	1	{0,3,4}	4	0	0	0	4	3	0	0	0	0	3	0	1	8	8	6	0	8	8	8	8	8	4	8	8	8	8	0	8	8	8	\N	8	8	8	8	8	8	5	8	2	5	3	8	0	1	1	0	0	1	{1,2}	1	13	7	2	7	7	7	5	0	1	2	0	1	8	0	\N	2	\N	8	0	4	0	\N	8	\N	\N	0	1	0	4	0	\N	7	0	0	0	4	0	1	0	0	2018-11-06	5
110	122	4	0	1	0	3	6	0	0	4	3	2	4	0	2	4	0	3	1	1	5	5	2	1	3	0	1	0	1	2	0	5	0	2	1	1	\N	2	3	0	10	0	6	0	0	1	\N	2	3	1	0	1	1	{3,4}	7	1	1	1	5	3	4	3	0	1	3	8	8	4	1	5	0	0	5	5	0	0	5	2	0	8	3	1	1	2	5	5	0	0	0	3	0	6	2	5	2	3	5	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	5	2	2	0	3	0	0	2	0	8	1	\N	\N	\N	\N	2	6	0	1	0	0	5	0	0	0	0	0	2	0	1	\N	0	0	0	2	0	1	0	0	2018-11-06	1
111	123	5	0	0	4	0	\N	0	1	2	3	2	4	1	4	5	2	3	0	2	5	5	1	0	2	1	1	1	0	0	1	2	8	2	0	1	3	3	1	0	5	0	4	0	0	1	\N	1	2	2	1	1	1	{2,4}	0	1	1	1	4	2	0	0	1	3	0	0	0	6	5	0	1	0	5	3	5	0	6	4	2	3	4	1	4	4	7	5	0	0	0	5	0	7	5	7	1	1	7	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	0	2	1	0	0	0	1	6	6	1	\N	\N	\N	\N	0	0	1	4	0	0	3	1	3	7	0	0	4	0	1	\N	0	0	0	2	0	1	4	3	2018-11-06	0
112	125	2	0	0	4	1	\N	1	0	4	3	4	4	0	4	4	0	0	0	0	4	5	2	0	2	0	1	1	0	0	0	0	5	1	1	1	\N	0	0	1	7	1	6	0	0	1	1	0	2	2	1	1	0	{4}	4	1	\N	0	0	3	0	0	0	0	0	0	2	5	1	1	0	2	5	5	0	0	6	2	3	\N	2	1	1	1	1	2	5	3	3	6	6	1	4	5	4	1	1	5	\N	\N	\N	\N	\N	1	{}	\N	\N	2	\N	2	4	4	6	0	4	4	4	1	\N	\N	\N	\N	\N	\N	1	0	0	0	7	\N	0	0	2	0	2	0	1	\N	\N	\N	\N	\N	0	4	1	4	2018-11-06	4
106	115	3	0	0	3	2	6	1	1	1	0	4	4	1	4	5	1	3	0	0	0	\N	0	0	1	0	1	1	0	0	0	0	9	1	1	1	\N	0	0	1	0	0	4	1	1	1	\N	1	3	0	1	1	1	{4}	7	1	\N	1	0	2	0	0	0	3	0	6	0	0	3	0	0	0	5	6	0	0	5	0	0	8	2	0	5	0	1	8	3	0	5	5	0	5	5	6	0	0	0	0	0	3	4	1	\N	1	{1}	0	13	3	3	2	1	1	0	0	1	1	0	1	\N	\N	\N	\N	0	0	0	0	0	0	0	0	0	0	1	0	0	0	1	\N	0	\N	\N	\N	\N	4	2	3	2018-11-06	0
239	298	3	1	2	2	2	6	1	1	2	1	3	4	0	4	4	0	2	1	1	3	3	2	0	2	1	0	0	0	0	0	7	8	1	1	1	\N	2	0	0	0	0	4	0	0	1	\N	2	2	3	1	1	1	{4}	3	0	0	0	4	2	0	4	1	4	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	6	\N	\N	\N	0	0	3	1	0	1	\N	\N	\N	\N	\N	\N	1	1	0	0	7	1	2	7	1	0	1	1	1	\N	0	0	0	0	0	2	0	0	2018-09-14	7
240	300	4	1	0	1	0	\N	0	0	1	3	4	4	0	3	4	0	2	0	0	4	5	4	1	2	0	1	0	0	0	0	0	\N	0	1	1	\N	0	0	0	6	0	5	0	1	2	\N	0	3	0	1	1	1	{1,4,6}	1	1	1	0	0	2	0	4	0	2	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	2	6	2	2	2	1	1	2	4	2	0	9	4	1	2	0	0	1	4	1	0	7	2	3	1	0	0	3	1	1	\N	0	0	0	2	0	4	3	3	2018-09-14	1
113	124	4	0	2	3	3	2	1	0	0	\N	4	4	0	4	2	1	1	0	0	4	0	3	0	3	0	0	1	2	1	0	0	9	\N	1	1	\N	1	0	1	\N	2	12	0	1	1	\N	1	2	1	1	1	1	{3,4}	7	1	1	1	5	3	4	4	0	2	0	6	1	1	1	1	0	2	6	4	1	1	6	6	1	6	6	0	3	1	1	3	3	2	2	1	1	2	4	3	2	3	3	3	0	5	1	0	0	1	{0}	0	9	6	1	5	2	0	1	1	3	1	0	1	\N	0	0	0	0	0	0	0	0	1	\N	0	0	0	\N	0	5	0	1	\N	0	\N	0	5	0	4	3	1	2003-11-20	2
114	126	5	0	0	1	1	6	1	0	1	0	4	4	1	2	1	1	0	0	0	0	0	0	0	1	0	1	1	1	0	0	0	\N	0	1	1	\N	2	0	1	\N	2	\N	0	0	2	\N	3	3	1	1	1	1	{6}	1	1	1	1	0	2	4	4	0	4	0	0	1	3	0	1	0	0	1	0	0	0	3	1	1	5	2	0	1	1	1	3	2	0	0	0	0	0	3	1	1	1	3	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	0	0	\N	0	1	0	4	1	\N	\N	\N	\N	1	0	0	4	2	0	4	0	1	\N	0	0	5	0	1	\N	0	\N	\N	\N	0	3	0	2	2018-11-06	0
115	127	4	0	2	1	3	0	0	0	0	1	1	4	0	4	5	0	0	0	0	3	5	3	3	1	6	0	1	1	2	0	0	\N	2	1	1	\N	0	1	1	10	0	12	0	0	0	\N	0	2	0	1	1	1	{5}	7	1	1	0	4	3	0	0	0	0	2	6	6	0	0	1	1	1	3	3	0	0	3	0	2	7	7	1	3	0	2	4	3	1	6	7	0	0	1	1	1	1	4	1	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	\N	2	4	7	6	0	4	7	5	0	4	0	0	0	0	0	0	1	0	0	3	\N	\N	\N	0	0	5	1	0	6	\N	\N	\N	\N	0	1	2	0	2018-11-06	7
116	129	3	0	0	2	3	2	1	0	3	3	2	4	0	2	3	0	0	0	0	1	5	0	0	2	0	1	1	0	0	0	0	\N	1	1	1	\N	3	0	0	0	0	12	0	0	2	1	1	3	0	1	1	1	{3}	4	0	1	1	4	2	4	0	0	0	0	8	0	0	0	\N	0	0	8	0	0	0	6	6	0	1	5	0	3	0	2	8	0	0	0	0	0	0	4	5	0	1	5	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	1	0	\N	0	2	1	8	1	\N	\N	\N	\N	0	0	0	4	2	0	7	0	0	0	1	0	1	0	1	\N	\N	\N	\N	5	0	0	0	1	2018-11-06	0
117	128	3	0	2	0	1	6	1	1	3	1	4	4	1	4	5	0	0	0	0	5	0	0	0	2	0	1	1	0	0	0	0	8	0	1	0	\N	2	3	1	1	2	0	0	0	1	0	3	3	3	1	0	1	{3}	4	0	0	1	5	2	0	0	0	4	0	5	1	4	2	5	1	0	5	6	0	5	6	1	2	0	1	1	2	0	0	5	0	6	6	8	0	5	4	0	2	1	1	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	3	2	0	3	6	0	1	1	8	1	\N	\N	\N	\N	0	\N	0	0	0	0	6	0	0	0	0	0	1	0	1	\N	\N	\N	\N	5	0	0	4	1	2018-11-06	3
118	131	4	0	0	1	1	6	1	1	0	3	2	4	0	4	3	1	1	0	0	2	5	0	4	2	0	1	1	0	0	0	0	\N	1	1	1	\N	1	0	1	\N	\N	\N	0	0	0	\N	0	1	0	1	1	1	{4}	4	1	\N	1	0	2	0	0	0	0	0	0	0	0	4	2	0	2	0	0	0	0	5	0	0	5	2	0	0	2	0	8	0	0	0	8	0	1	3	0	3	1	5	0	0	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	0	0	1	0	1	3	8	1	\N	0	0	0	0	0	0	0	0	\N	3	0	0	0	0	0	2	0	1	\N	0	0	\N	5	0	4	0	0	2018-11-06	0
119	130	4	1	2	0	3	6	0	0	2	2	1	4	0	4	3	1	0	0	0	2	5	4	2	2	0	1	0	0	0	0	0	\N	1	1	1	\N	2	0	0	0	0	12	0	0	1	1	1	2	0	1	1	1	{3}	1	1	1	1	4	2	4	0	0	0	0	1	5	1	1	0	0	4	8	2	0	1	6	3	2	5	2	1	3	4	2	8	1	0	6	7	0	6	2	3	1	2	6	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	0	0	0	0	1	4	8	0	7	0	0	0	2	6	1	3	0	0	7	3	6	8	1	0	4	0	0	7	0	0	\N	3	1	0	0	0	2018-11-06	0
120	134	3	0	0	3	0	\N	1	1	1	3	2	4	1	4	3	1	\N	0	0	4	5	0	0	1	0	1	1	0	0	0	0	\N	\N	1	1	\N	2	1	0	0	0	12	0	0	1	\N	2	1	0	1	1	1	{6}	6	1	\N	1	0	2	0	4	0	1	0	0	3	3	1	0	0	2	1	3	0	0	6	0	0	3	2	0	1	1	0	2	0	2	4	3	0	1	3	3	0	1	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	0	0	\N	0	1	2	6	1	\N	\N	\N	\N	\N	0	0	0	0	1	\N	\N	\N	\N	\N	\N	0	0	1	\N	\N	\N	\N	0	0	4	0	1	2018-11-05	0
121	132	3	0	2	2	2	6	0	0	2	3	4	4	0	4	3	1	0	\N	\N	5	5	0	\N	2	\N	1	1	2	1	\N	0	5	1	1	1	\N	1	1	0	1	0	12	0	1	1	\N	1	2	2	1	1	1	{5}	6	0	0	1	5	4	4	0	1	0	0	6	5	5	5	2	0	2	5	5	2	0	6	2	0	5	2	0	5	2	0	6	6	1	5	6	0	0	3	5	6	5	5	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	4	5	6	0	4	3	6	0	3	0	0	0	0	0	0	0	0	0	6	0	0	0	0	0	0	0	1	\N	0	0	0	0	0	1	1	0	2018-11-06	5
122	133	4	0	1	1	2	6	1	0	1	2	2	3	0	3	5	1	3	0	0	5	5	0	2	1	0	1	1	0	0	0	0	\N	1	1	1	\N	1	0	0	1	0	6	0	0	1	\N	1	2	0	1	1	1	{4}	7	1	\N	1	4	4	2	0	0	0	0	3	3	0	1	0	0	0	1	1	0	0	6	3	0	5	3	1	3	3	0	6	1	3	3	3	0	3	1	3	0	1	3	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	1	0	\N	0	2	3	8	1	\N	\N	\N	\N	0	0	1	0	0	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	5	0	3	0	2	2018-11-06	0
123	135	2	0	4	1	2	6	0	0	2	3	4	4	0	2	2	2	1	0	1	5	5	4	4	1	\N	1	1	1	1	\N	0	\N	2	1	1	\N	0	1	1	10	1	2	0	0	1	\N	0	2	0	0	1	1	{3}	4	1	1	1	0	3	0	0	0	0	0	2	2	5	2	0	0	0	5	0	2	0	7	1	1	5	6	1	5	1	2	8	0	6	5	6	5	5	3	5	0	1	0	5	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	2	5	4	6	0	4	9	8	1	\N	\N	\N	\N	0	0	0	1	0	0	0	1	1	4	0	0	3	0	1	\N	0	0	0	0	0	4	2	0	2018-11-06	2
107	116	3	1	0	1	0	\N	1	1	1	3	4	4	0	4	4	0	1	1	0	0	5	0	0	1	0	1	1	0	0	0	0	\N	1	1	1	\N	2	1	1	5	0	12	0	0	1	\N	3	1	2	1	1	1	{0,6}	4	1	1	1	4	2	4	0	0	0	3	2	0	0	1	0	0	1	1	3	0	0	4	1	2	5	1	1	1	1	1	3	2	2	5	3	0	2	3	2	0	0	8	0	0	5	7	0	5	1	{2}	0	\N	5	2	2	0	0	\N	0	1	2	3	0	7	0	0	\N	1	\N	1	4	0	0	7	0	2	4	0	0	2	1	1	\N	0	0	0	0	0	\N	3	1	2018-11-06	0
124	136	5	0	0	4	0	\N	1	1	0	3	2	4	1	4	5	1	3	0	0	3	5	0	0	1	0	1	1	0	0	0	0	0	1	1	1	\N	0	2	0	5	0	12	0	0	1	\N	1	1	2	1	1	1	{4}	4	1	1	1	4	2	0	0	1	3	0	2	7	2	3	1	0	1	3	3	1	0	6	5	2	2	3	0	4	4	1	5	4	5	4	5	1	4	4	4	1	1	5	2	\N	\N	\N	\N	\N	1	{}	\N	\N	1	1	2	1	0	0	0	1	4	6	1	\N	\N	\N	\N	0	0	0	4	0	1	\N	\N	\N	\N	\N	\N	3	1	1	\N	0	0	0	1	0	1	2	3	2018-11-06	0
125	137	4	1	2	3	0	6	1	0	3	3	1	4	0	4	5	2	0	0	0	2	5	0	0	1	0	1	1	0	0	0	0	8	1	1	1	\N	1	0	1	10	2	12	0	0	1	\N	3	3	1	1	1	1	{4,7}	1	1	1	1	4	2	3	0	0	2	0	5	1	5	1	1	0	2	3	1	1	0	6	3	0	5	2	1	4	3	0	8	1	2	5	5	1	2	7	5	2	1	5	1	0	\N	7	0	8	0	{2}	1	\N	0	1	2	0	5	1	0	4	5	8	0	6	0	0	0	0	0	1	1	0	0	6	0	0	0	1	0	3	0	1	\N	\N	\N	\N	\N	\N	3	1	2	2018-11-06	1
126	138	4	0	0	1	0	\N	1	1	0	0	4	4	0	4	4	0	1	0	0	5	5	4	2	1	0	1	1	0	2	0	0	\N	1	1	1	\N	1	1	1	6	0	4	0	1	0	\N	2	0	2	0	1	0	{0}	5	0	0	1	4	2	4	5	0	3	0	2	3	4	0	1	0	1	3	3	1	0	6	5	5	5	3	0	2	3	1	6	2	5	6	5	1	5	4	5	1	1	0	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	2	1	5	0	\N	0	1	1	0	1	\N	\N	\N	\N	0	0	0	3	0	0	6	0	0	1	0	0	3	0	1	\N	\N	\N	\N	\N	0	4	0	1	2018-11-07	0
127	139	3	1	0	3	0	\N	1	1	0	3	2	4	0	2	4	1	2	0	\N	5	5	\N	\N	2	\N	\N	\N	0	0	0	0	\N	1	1	1	\N	1	2	0	0	0	6	0	0	1	\N	1	1	0	1	1	1	{4}	4	1	1	1	0	0	0	0	0	0	0	5	2	2	3	1	0	0	3	3	0	0	6	0	0	5	2	0	5	0	5	3	1	3	4	3	0	3	4	2	1	2	2	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	0	1	0	0	2	2	2	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	\N	3	1	3	2018-11-07	0
128	140	4	0	4	2	2	3	1	0	0	3	3	4	1	3	5	1	0	0	0	3	0	0	0	1	0	1	1	1	1	1	7	2	0	1	1	\N	1	0	1	\N	2	0	0	0	1	\N	2	2	2	1	1	1	{7}	4	0	0	1	0	2	0	5	0	0	0	6	0	0	0	0	0	0	0	1	0	0	6	0	1	5	1	0	2	0	1	6	1	2	6	3	0	3	4	4	1	1	1	3	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	7	3	6	1	0	0	3	1	\N	\N	\N	\N	0	0	0	0	0	0	5	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	\N	0	1	4	2018-11-07	1
129	141	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	4	1	\N	1	0	\N	0	4	0	0	0	6	7	0	0	0	0	0	0	0	0	0	1	0	0	1	1	\N	1	0	0	0	0	0	0	0	0	0	3	8	0	5	8	0	\N	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-05	\N
130	142	2	0	1	2	0	\N	1	1	0	3	4	4	0	4	4	1	0	1	0	3	4	0	1	2	0	1	1	0	0	0	0	\N	0	1	1	\N	2	1	1	\N	0	12	0	1	0	\N	0	2	0	1	1	\N	{}	1	1	1	0	0	1	0	4	0	3	0	1	3	3	2	0	1	1	\N	1	0	0	4	3	1	1	1	1	2	2	1	3	1	3	3	3	0	4	4	4	1	1	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	1	4	2	2	0	1	2	2	1	\N	\N	\N	\N	0	0	1	1	4	0	7	0	0	0	1	0	1	0	1	\N	\N	\N	\N	\N	\N	3	2	1	2018-11-07	2
131	144	4	0	0	4	0	\N	0	0	2	3	1	4	1	4	4	1	3	3	0	3	2	3	0	1	0	0	1	0	0	0	0	9	1	1	1	\N	0	\N	1	\N	1	\N	0	1	0	\N	2	1	1	1	1	1	{4}	6	1	1	1	5	2	1	4	0	0	0	3	3	0	3	0	1	0	3	0	0	0	4	3	3	4	4	0	3	2	4	8	4	4	0	4	0	4	3	4	4	4	4	3	\N	\N	\N	\N	\N	0	{}	\N	\N	1	2	1	7	0	2	0	2	1	\N	0	5	0	0	0	1	0	0	0	4	1	\N	0	0	0	0	0	0	0	1	\N	\N	\N	\N	0	0	4	0	2	2018-11-07	0
132	143	3	0	3	2	0	\N	1	1	2	2	1	0	1	4	3	1	2	0	0	3	0	0	0	2	0	1	1	0	1	0	0	\N	\N	1	1	\N	2	1	0	0	0	12	0	1	1	\N	1	1	2	1	1	1	{2}	1	1	\N	1	0	2	0	4	0	0	0	6	5	0	0	1	0	1	3	3	0	0	6	2	0	6	5	0	2	2	0	7	1	0	0	5	0	6	4	3	3	0	6	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	6	5	1	1	4	3	1	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	\N	0	0	0	1	\N	0	0	\N	0	0	4	3	1	2018-11-05	1
241	301	2	1	2	2	0	\N	1	1	2	3	4	2	0	4	5	0	3	1	0	2	0	4	1	1	2	1	1	0	0	0	0	0	0	1	1	\N	0	4	0	0	0	\N	0	\N	0	\N	0	2	0	1	0	0	{3}	\N	1	1	0	0	0	0	1	1	1	2	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	0	3	\N	\N	0	0	1	0	5	1	\N	\N	\N	\N	\N	\N	1	\N	\N	1	0	0	\N	\N	0	0	0	1	1	\N	\N	\N	\N	0	\N	4	4	2	2018-09-14	1
133	146	4	0	0	2	0	6	1	0	1	0	4	4	0	4	4	0	1	0	0	3	0	4	2	4	0	1	1	0	3	0	2	5	2	1	0	\N	1	3	0	0	1	2	0	0	2	0	1	1	2	1	1	0	{3}	5	0	0	1	0	1	0	5	0	0	0	3	3	0	1	2	1	1	1	0	1	7	4	3	3	0	6	0	4	3	0	2	2	1	2	3	4	5	9	3	3	2	5	2	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	1	7	0	0	0	4	1	1	1	\N	\N	\N	\N	0	0	0	0	0	0	7	0	0	0	0	0	5	0	1	\N	\N	\N	\N	\N	0	4	1	4	2018-11-07	5
134	145	5	0	1	3	0	\N	1	1	2	3	4	4	0	3	4	0	0	0	0	3	5	0	0	3	0	1	1	1	0	0	0	\N	1	1	1	\N	2	1	0	5	0	11	0	1	2	\N	3	3	1	1	1	1	{2}	5	1	1	1	4	2	0	4	0	0	0	0	3	1	0	1	1	1	0	0	0	0	5	1	1	3	1	1	1	1	0	3	3	6	0	3	0	5	4	3	1	1	3	3	\N	\N	\N	\N	\N	1	{}	\N	\N	3	3	4	3	1	0	0	1	4	0	0	8	1	7	0	2	2	0	1	0	0	7	0	0	0	2	0	3	0	1	\N	\N	\N	\N	\N	0	4	0	0	2003-05-09	0
135	147	1	1	4	2	0	\N	1	1	0	3	4	4	0	4	3	1	2	0	0	5	5	0	0	1	0	1	0	0	0	0	0	\N	0	1	1	\N	2	0	1	5	1	4	0	1	1	0	1	1	0	1	1	1	{4}	7	1	1	0	0	2	0	5	0	0	0	3	0	0	1	1	1	2	1	3	0	0	2	0	0	3	0	1	0	2	1	5	2	3	1	6	1	3	4	3	3	0	0	5	0	\N	\N	\N	\N	1	{}	\N	\N	0	0	1	3	0	1	1	1	0	\N	1	3	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	1	2	1	2	2018-11-05	0
136	148	3	1	0	4	0	6	1	0	0	3	3	4	0	4	3	1	0	0	0	0	5	0	0	1	0	1	1	0	0	0	0	8	2	1	1	\N	0	0	1	0	1	12	0	0	0	1	0	2	0	1	1	1	{4}	3	1	1	0	0	3	0	0	1	4	0	7	1	0	0	1	0	0	8	1	0	0	8	1	1	8	8	0	0	0	8	8	1	3	0	1	0	1	3	8	0	0	6	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	1	\N	0	\N	0	2	3	3	1	\N	\N	\N	\N	\N	\N	1	\N	3	1	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	0	4	4	4	2018-11-05	0
137	150	4	0	0	3	0	\N	1	0	1	3	0	4	1	4	3	0	0	0	0	5	\N	\N	0	1	0	1	1	0	0	0	0	\N	0	1	1	\N	1	0	0	0	0	0	0	0	0	\N	1	1	3	1	1	1	{3}	4	1	1	1	0	0	0	2	0	0	0	2	0	0	1	0	0	1	3	0	0	0	4	3	3	3	3	0	1	0	0	4	1	0	4	1	0	1	5	7	0	0	1	0	\N	\N	\N	\N	\N	1	{}	\N	\N	1	2	1	6	0	\N	0	2	6	0	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	0	0	4	2	1	2018-11-05	2
138	149	2	1	4	3	1	6	1	1	0	3	4	4	1	2	5	1	3	0	0	3	5	0	0	1	0	1	1	0	0	0	0	\N	2	1	1	\N	1	0	1	\N	1	\N	0	1	0	\N	0	2	1	0	1	1	{4}	2	0	0	0	0	2	0	5	0	1	0	5	6	1	0	0	0	1	3	2	0	1	6	0	0	2	2	1	1	2	1	5	0	2	5	6	0	3	2	2	0	2	0	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	1	0	0	\N	0	2	0	0	1	\N	\N	\N	\N	\N	0	1	1	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	0	4	3	4	2018-11-07	0
139	151	4	1	1	1	1	6	1	0	3	1	2	2	0	4	3	1	0	0	3	0	5	3	1	1	0	1	1	3	0	0	0	8	0	0	1	4	1	2	0	0	0	4	0	0	0	\N	1	0	0	1	1	1	{3}	4	1	1	1	0	2	0	0	0	1	0	0	0	1	3	3	0	1	5	5	1	1	7	1	1	6	1	1	1	1	1	6	2	2	6	6	1	2	3	7	1	1	7	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	5	1	1	0	1	6	0	1	9	8	0	0	5	4	0	6	6	1	4	0	0	0	4	4	4	1	0	3	0	1	\N	\N	\N	\N	\N	1	1	0	1	2018-11-05	2
140	152	4	0	0	3	4	3	1	0	2	3	0	4	1	4	5	2	0	3	2	5	5	0	0	2	2	1	0	0	0	0	0	5	0	1	1	\N	0	1	1	\N	2	\N	0	0	2	\N	3	3	1	1	1	1	{4}	1	1	1	0	0	2	0	0	0	0	0	6	0	0	0	0	0	1	6	0	0	0	6	5	2	6	0	0	0	0	0	6	1	6	6	6	0	5	3	6	1	5	7	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	1	5	4	4	0	0	7	5	0	6	0	0	0	1	0	0	4	1	0	5	0	1	4	1	0	2	0	1	\N	\N	\N	\N	\N	1	4	0	0	2018-11-07	0
141	154	4	1	4	0	0	\N	1	1	2	2	1	3	1	3	4	2	0	3	0	4	5	0	4	1	0	1	1	0	0	0	0	\N	1	1	1	\N	0	1	1	0	1	12	0	1	1	\N	1	2	0	1	1	1	{3}	0	1	\N	1	4	2	0	0	0	0	1	0	1	2	3	0	0	2	4	6	1	0	6	8	3	3	3	1	0	4	1	6	2	2	6	8	1	5	9	8	3	3	7	3	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	7	0	\N	0	0	2	4	1	\N	0	0	0	0	0	0	3	0	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	0	3	1	4	2018-11-07	0
142	153	5	1	0	2	0	0	1	1	4	2	4	4	0	4	4	1	0	0	0	2	4	0	0	2	0	1	1	0	0	0	0	\N	1	1	1	\N	0	1	1	0	0	6	1	1	2	\N	1	1	2	1	1	0	{4}	3	1	\N	0	0	2	0	0	0	4	0	5	3	0	2	2	0	3	4	4	0	0	2	2	2	4	1	0	3	1	3	6	4	1	6	4	2	4	7	4	7	1	8	4	\N	\N	\N	\N	\N	1	{}	\N	\N	5	2	1	0	0	\N	0	1	5	3	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	0	\N	1	0	1	\N	\N	\N	\N	1	0	4	0	0	2018-11-07	0
143	155	4	0	1	1	0	3	1	0	2	1	4	4	0	4	5	1	0	0	0	2	4	2	0	1	0	1	1	0	1	0	0	1	1	1	1	\N	0	0	1	\N	2	\N	0	0	3	\N	3	3	0	1	1	1	{4}	4	1	1	1	1	2	0	4	0	4	0	3	0	0	0	1	0	1	2	1	1	0	2	3	2	3	3	0	0	1	0	8	0	3	4	3	0	1	4	4	1	1	5	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	4	0	1	1	0	0	1	0	1	\N	\N	\N	\N	0	0	1	1	0	1	\N	0	0	0	0	0	3	1	1	\N	0	0	0	2	0	4	1	3	2018-11-07	0
144	156	3	0	0	4	0	0	1	0	0	3	4	4	1	4	5	2	0	2	0	3	5	0	0	4	0	1	1	0	0	0	0	0	0	1	1	\N	1	0	1	\N	2	\N	0	1	1	\N	1	2	0	1	1	1	{4}	4	1	\N	1	0	2	4	5	0	0	0	5	\N	5	1	5	1	1	5	1	0	0	5	0	0	1	\N	0	\N	\N	\N	5	6	6	6	5	5	5	7	6	0	0	0	0	\N	\N	\N	\N	\N	0	{}	\N	\N	7	1	1	5	0	0	0	1	0	0	1	\N	0	0	0	\N	0	1	4	0	1	\N	0	0	\N	0	0	5	0	1	\N	0	0	0	0	1	4	2	4	2018-11-07	1
145	159	1	1	0	4	0	\N	1	0	3	3	4	2	0	4	3	1	0	0	0	5	5	0	0	1	0	0	1	0	0	0	0	\N	1	1	1	\N	0	1	1	9	2	12	0	0	0	\N	0	2	1	1	1	1	{4}	7	1	1	1	0	2	0	0	0	3	0	3	3	1	3	3	0	1	1	3	1	1	6	2	0	3	5	0	3	2	2	5	2	5	5	5	1	1	4	5	2	1	4	0	\N	\N	\N	\N	\N	1	{}	\N	\N	1	3	1	3	0	\N	0	3	9	7	\N	\N	0	0	0	3	6	0	4	1	\N	\N	0	0	0	0	0	2	0	1	\N	0	0	0	2	0	4	1	1	2018-11-07	0
146	160	4	0	0	3	0	\N	1	0	3	2	3	4	0	2	4	1	0	0	0	5	5	2	0	2	0	1	1	2	0	0	7	9	1	0	1	2	1	3	0	0	0	12	0	0	1	\N	1	2	2	1	1	1	{4}	6	1	1	1	0	2	0	5	0	2	0	3	3	2	3	2	0	2	3	3	1	3	4	1	1	3	2	1	2	1	0	4	1	3	3	4	0	3	2	1	1	0	3	2	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	\N	2	4	0	\N	0	1	4	2	1	\N	\N	\N	\N	0	0	0	0	1	0	5	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	0	3	2	3	2004-03-15	0
147	161	3	1	0	3	2	3	1	0	2	3	4	4	1	4	4	0	0	5	3	4	5	0	0	1	0	1	1	0	0	0	0	\N	2	1	1	\N	1	2	1	\N	2	\N	\N	\N	1	\N	1	2	1	1	1	1	{4}	4	1	1	1	4	2	0	0	0	3	0	1	1	4	1	4	0	1	1	4	0	0	4	0	1	1	1	1	1	1	1	5	0	5	5	5	0	1	1	1	1	1	2	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	1	2	0	0	0	1	7	6	1	\N	\N	\N	\N	\N	\N	1	0	1	0	8	0	0	0	\N	0	2	1	1	\N	\N	\N	\N	\N	0	4	3	4	2018-11-07	0
148	158	0	0	2	1	2	6	0	1	4	3	4	4	0	4	4	0	3	0	0	5	5	2	1	1	0	0	0	1	1	1	0	0	2	1	1	4	1	3	0	0	0	4	0	1	0	\N	0	2	0	0	0	0	{3}	1	1	1	0	0	2	0	0	0	0	0	6	6	2	0	1	1	6	6	6	1	0	6	1	1	6	6	1	3	1	1	6	6	6	6	6	6	7	4	7	3	6	7	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	2	7	7	6	0	1	1	1	0	0	1	6	0	0	0	1	0	0	0	9	1	1	4	4	0	3	0	1	\N	\N	\N	\N	0	1	3	2	4	2018-11-07	0
149	163	4	1	0	1	2	3	1	0	2	3	2	4	0	4	5	0	0	1	0	5	5	0	0	1	0	1	1	0	0	0	0	\N	0	1	1	\N	0	2	1	9	0	0	0	0	0	\N	0	3	1	1	1	1	{0}	1	1	1	0	0	2	0	0	0	1	0	4	4	5	4	0	0	5	5	5	5	0	6	5	6	5	5	0	6	6	5	7	0	0	5	8	7	7	2	6	5	5	5	5	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	4	3	0	0	1	2	1	2	1	\N	\N	\N	\N	0	0	1	2	0	0	6	1	1	4	1	0	4	0	1	\N	\N	\N	\N	\N	1	2	2	4	2018-11-07	0
150	162	4	1	2	4	1	3	1	0	1	2	3	3	0	4	5	1	3	0	0	3	5	4	2	1	0	1	1	0	2	0	7	0	1	1	1	\N	1	1	0	1	0	2	0	0	1	1	3	2	0	1	1	1	{0,6}	6	1	1	1	2	2	1	0	0	0	0	3	3	3	1	1	0	1	2	1	1	0	6	0	1	1	1	1	2	1	1	6	1	0	5	5	0	1	2	1	2	2	3	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	2	7	4	3	0	1	4	6	0	6	0	0	0	1	0	0	1	0	0	4	2	6	1	4	1	3	0	1	0	0	0	0	1	1	1	2	1	2003-10-07	2
151	165	4	0	0	3	0	\N	1	0	0	3	3	4	0	4	1	1	0	0	0	5	5	0	0	2	0	1	1	0	0	0	0	\N	\N	1	1	\N	0	1	0	0	0	12	0	0	0	\N	0	2	2	1	1	1	{0}	1	1	1	0	0	2	0	0	0	4	0	0	0	0	1	1	0	3	3	4	1	2	4	3	3	4	3	0	3	3	3	4	4	3	4	5	0	4	7	1	1	2	3	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	1	0	0	\N	0	1	3	3	1	\N	\N	\N	\N	\N	0	1	0	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	\N	4	0	1	2018-11-07	0
152	164	1	1	0	3	0	\N	1	0	1	3	4	4	1	4	5	1	2	0	0	3	5	4	4	1	0	1	1	0	0	0	2	7	2	1	\N	\N	0	2	0	0	1	4	0	0	0	1	0	2	3	1	1	1	{3}	0	0	0	0	0	2	4	0	0	0	0	1	2	2	1	2	1	0	2	3	0	0	5	0	0	5	5	1	6	0	0	2	0	5	5	5	0	6	3	6	0	0	5	5	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	4	7	0	1	0	1	0	0	1	\N	\N	\N	\N	0	0	1	4	0	0	0	0	0	0	0	0	3	0	1	\N	0	0	0	1	0	2	0	2	2018-11-07	0
153	167	4	\N	1	0	0	\N	1	1	1	2	3	3	0	2	4	1	2	0	0	0	\N	0	0	2	0	1	\N	0	0	0	0	\N	1	1	1	\N	0	0	1	\N	1	\N	0	1	0	\N	1	2	2	1	1	1	{0}	4	1	\N	1	0	2	3	0	0	3	0	3	3	3	3	3	0	3	3	3	5	3	5	2	2	5	3	1	3	3	3	3	3	3	3	3	3	3	4	3	3	2	3	3	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	7	0	\N	0	4	4	6	1	\N	\N	\N	\N	0	0	0	0	4	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	1	2	2	1	2018-11-07	2
242	302	1	0	0	2	0	\N	1	1	1	2	4	4	1	4	4	0	\N	0	0	0	0	0	3	0	0	1	1	0	0	0	0	\N	0	1	1	\N	0	0	1	\N	2	\N	0	0	0	\N	0	2	2	1	1	1	{0}	1	1	0	0	0	2	0	4	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	\N	\N	\N	\N	1	1	1	0	1	\N	\N	\N	\N	\N	\N	0	\N	\N	1	\N	0	0	0	0	0	2	0	1	\N	0	0	0	5	0	\N	2	2	2018-05-14	1
154	166	5	0	4	4	0	\N	1	1	0	1	2	4	0	2	4	1	3	0	0	5	3	2	1	2	0	1	1	0	0	0	0	\N	1	1	1	\N	0	1	0	0	0	\N	0	0	0	\N	0	2	0	1	1	1	{2}	1	1	\N	0	0	2	0	0	0	0	0	1	5	5	5	5	0	5	6	3	2	3	4	6	3	6	7	1	7	6	1	6	6	5	7	7	2	2	4	6	3	3	5	6	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	1	1	0	0	1	0	9	2	1	\N	\N	\N	\N	\N	\N	1	1	0	0	8	0	0	4	1	0	4	1	1	\N	\N	\N	\N	0	\N	4	0	4	2018-11-07	0
155	168	4	1	1	3	2	6	0	0	1	3	2	4	0	2	5	1	0	0	0	3	5	0	0	1	0	1	1	0	0	0	0	8	1	1	1	\N	2	4	1	10	0	6	0	1	1	\N	1	2	2	1	1	1	{4}	1	1	\N	1	0	2	0	0	0	2	0	7	3	2	1	0	0	3	3	1	2	0	4	4	0	4	4	0	3	2	1	3	1	3	0	3	4	2	4	0	1	3	4	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	1	7	0	4	0	2	2	1	0	5	0	0	0	0	0	1	2	0	1	8	0	\N	\N	\N	\N	\N	0	\N	9	0	0	0	3	4	2	0	2	2018-11-07	2
156	208	4	0	4	0	2	6	0	0	2	3	3	4	1	2	4	2	3	0	0	5	0	1	1	2	0	1	1	1	1	0	0	\N	1	1	1	\N	1	2	0	1	0	4	0	1	1	\N	3	3	1	1	1	1	{6}	\N	1	1	1	0	2	4	0	0	0	0	2	3	3	1	3	0	2	4	2	2	1	5	2	2	3	3	0	1	1	1	2	1	5	5	3	0	3	4	3	0	2	6	1	0	5	7	0	\N	1	{2,3}	1	\N	0	\N	2	0	0	\N	0	2	3	5	\N	\N	\N	\N	\N	2	6	0	0	0	0	6	1	2	8	0	0	2	0	1	\N	0	0	0	0	1	0	0	2	2018-11-06	\N
157	206	5	0	0	1	0	6	\N	0	2	3	3	3	0	3	5	0	1	0	0	5	5	1	0	1	0	0	0	0	2	0	0	\N	1	1	1	\N	2	1	0	0	0	11	0	0	2	\N	1	2	0	1	1	1	{3}	7	1	1	1	0	4	0	0	0	0	0	0	0	2	2	0	0	1	1	0	0	0	6	2	2	0	2	\N	5	0	2	5	0	0	0	6	0	0	3	6	5	0	7	0	0	5	5	1	\N	1	{3}	1	\N	0	\N	2	0	2	6	0	3	8	\N	0	3	2	3	1	2	\N	1	4	0	0	0	1	2	4	1	0	4	0	0	6	0	0	0	4	0	2	0	2	2018-11-06	5
158	207	5	1	0	2	0	\N	1	1	0	3	1	3	1	3	5	1	0	0	0	2	0	0	0	1	0	1	1	1	1	0	0	\N	1	0	1	\N	1	1	0	3	0	4	0	0	0	\N	1	1	0	1	0	0	{4}	7	1	\N	1	0	0	0	4	0	0	0	1	1	2	1	1	0	1	5	3	1	1	5	1	1	3	3	0	1	1	0	4	3	2	2	3	0	2	5	2	1	1	5	1	0	0	0	0	9	1	{2,3}	0	\N	0	\N	2	0	0	0	1	1	0	6	1	\N	0	0	0	1	\N	1	1	3	0	6	0	0	0	\N	1	5	0	1	\N	0	0	0	5	1	2	0	4	2018-11-06	0
159	209	3	0	2	3	1	6	0	0	3	3	1	4	0	3	5	1	0	0	0	4	4	2	1	1	0	1	0	2	1	0	7	5	2	1	1	\N	2	1	0	6	1	2	0	1	1	\N	1	3	1	1	0	\N	{4,5}	6	0	1	\N	4	2	4	0	0	0	2	3	5	2	3	3	0	1	2	3	0	1	5	6	1	6	5	0	6	3	3	7	1	1	6	6	1	3	4	6	3	2	7	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	3	2	5	3	3	1	2	5	3	0	6	0	0	0	2	6	0	0	0	0	7	1	3	4	1	0	3	0	0	7	0	0	0	3	1	1	0	2	2018-11-08	2
160	210	3	1	2	1	2	3	0	0	1	3	1	4	1	1	2	1	0	0	3	3	0	0	0	1	1	1	1	1	2	2	1	8	1	1	1	\N	1	2	0	5	2	11	0	1	1	\N	1	2	1	1	1	1	{3}	5	0	0	0	1	0	3	2	0	0	0	5	4	6	3	1	0	1	2	2	1	1	5	1	1	3	3	0	2	1	1	6	1	4	6	6	2	1	5	1	2	1	2	1	0	5	1	0	8	1	{2,3}	0	\N	6	0	2	4	6	6	1	4	3	2	1	\N	\N	\N	\N	\N	0	1	1	0	0	4	0	0	0	0	0	2	1	1	\N	0	0	0	1	0	2	1	1	2018-11-06	5
161	212	\N	1	2	0	4	2	1	0	1	1	\N	4	1	4	5	0	3	0	0	0	0	0	0	1	0	1	1	5	0	0	7	9	0	1	1	\N	2	1	1	0	0	4	0	1	1	\N	1	3	3	0	0	\N	{3}	3	1	1	0	0	0	0	0	0	0	0	5	5	1	0	0	0	1	0	0	0	0	6	0	1	0	0	1	2	0	0	6	2	1	6	1	1	6	2	0	0	0	0	2	0	5	9	1	13	0	{2}	1	13	0	0	0	0	0	3	0	0	1	4	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	0	0	1	0	2018-11-06	0
162	211	3	0	4	4	4	\N	0	0	3	1	0	2	0	2	3	1	0	0	0	3	4	0	4	1	5	1	0	7	1	7	5	9	1	1	1	\N	3	2	0	\N	0	\N	0	0	3	\N	3	3	0	1	1	\N	{3,4,5}	6	1	\N	1	4	2	4	0	0	0	1	0	1	1	1	0	0	0	2	1	0	0	6	0	0	2	1	1	1	1	0	5	1	0	6	3	0	4	3	3	0	0	3	2	0	5	4	0	13	1	{1,2,3}	0	9	6	3	0	0	3	6	0	2	5	4	0	1	0	0	0	1	0	0	1	1	1	\N	\N	\N	\N	\N	\N	\N	1	0	\N	\N	\N	\N	3	0	3	0	0	2018-11-06	3
163	214	2	1	3	3	3	6	1	1	1	3	3	4	0	2	3	1	0	0	1	5	5	1	0	1	0	1	1	0	0	0	7	5	1	1	1	\N	1	1	1	6	0	2	0	0	1	\N	1	2	0	1	1	\N	{}	7	1	\N	1	4	0	0	0	0	0	0	4	4	4	2	1	0	3	3	4	1	2	6	3	3	2	1	1	2	1	1	5	2	5	5	5	1	1	2	2	2	1	2	1	0	3	0	0	7	\N	{2,3}	0	6	1	1	2	0	2	6	0	2	3	3	1	\N	\N	\N	\N	0	0	0	0	0	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	4	\N	2	1	2004-07-16	2
164	213	2	0	1	2	2	0	0	0	2	3	2	3	0	2	1	2	3	0	0	4	5	0	1	1	0	1	1	0	1	1	0	8	1	1	1	\N	1	1	0	3	1	12	0	1	0	\N	1	1	1	1	1	1	{4}	1	1	1	1	3	0	4	1	0	0	1	1	0	1	0	0	0	1	3	4	1	0	4	0	1	1	1	0	3	1	0	5	2	0	0	6	1	3	3	3	1	3	2	2	0	4	0	0	2	1	{2,3}	0	3	0	1	2	7	5	6	0	4	5	5	1	\N	\N	\N	\N	\N	\N	0	1	0	0	5	0	0	6	0	0	1	0	1	\N	0	0	0	5	0	1	0	2	2018-11-08	2
165	216	3	0	1	4	1	2	0	0	1	1	0	2	1	2	5	1	3	0	0	5	4	1	2	2	0	1	1	0	1	0	2	8	2	1	1	1	1	2	0	1	0	6	0	1	0	\N	3	3	0	0	1	1	{3,4}	6	1	\N	1	2	2	0	2	0	0	1	2	2	0	3	1	0	2	3	3	0	0	6	1	1	3	1	0	3	0	0	7	1	2	3	3	0	2	2	3	2	2	1	2	0	5	4	0	\N	1	{3}	0	\N	5	0	0	0	2	1	0	1	0	5	1	\N	\N	\N	\N	2	6	0	1	0	0	5	1	2	4	1	0	3	0	1	\N	\N	\N	\N	2	0	3	1	0	2018-11-06	0
166	215	3	0	0	3	2	6	0	0	1	3	2	4	0	2	3	2	0	0	0	5	5	4	\N	1	0	1	1	0	0	0	0	\N	1	1	1	\N	1	1	0	5	0	12	0	0	0	\N	1	2	0	1	1	1	{5}	3	1	\N	1	4	2	0	0	0	0	0	1	0	0	0	1	0	0	0	0	0	0	6	0	0	5	3	0	0	0	0	6	3	3	6	6	0	1	4	1	0	0	5	5	0	\N	\N	\N	\N	1	{}	\N	\N	7	0	2	5	2	6	1	2	5	\N	0	7	0	0	\N	\N	\N	1	\N	0	0	6	1	3	7	1	0	2	0	0	6	0	0	\N	1	0	4	0	0	2018-11-06	2
167	217	2	0	4	3	2	6	0	0	2	3	2	3	0	2	2	0	3	0	0	4	5	0	0	1	0	1	1	0	0	0	\N	\N	2	1	1	\N	2	1	0	9	2	\N	0	1	3	\N	1	0	3	1	1	1	{4}	7	1	\N	1	4	0	0	0	0	1	1	1	0	1	0	3	0	3	3	2	0	0	4	2	1	3	3	0	3	3	2	4	1	3	4	4	0	3	4	4	2	2	4	3	\N	\N	\N	\N	\N	1	{}	\N	\N	5	2	2	7	2	6	0	4	6	6	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	\N	\N	1	0	\N	\N	\N	\N	\N	0	1	4	2	2	2018-11-06	3
168	218	2	1	4	2	0	6	1	0	3	2	4	4	0	3	5	2	3	0	0	1	5	0	0	1	1	1	1	1	0	0	2	8	0	0	1	1	2	2	0	2	0	2	0	0	2	\N	3	3	1	1	\N	1	{0,4}	\N	1	1	1	4	2	4	5	0	0	0	8	0	1	0	0	0	0	0	2	0	0	5	2	0	0	2	\N	2	0	1	5	3	2	8	2	0	5	1	2	0	0	2	0	0	5	5	1	0	1	{2}	0	0	5	1	2	5	5	3	0	1	0	5	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	2	0	1	0	0	2018-11-06	2
169	221	1	0	2	4	2	6	0	1	0	3	4	4	1	4	5	0	3	1	1	5	5	0	0	1	0	1	1	0	0	0	0	8	2	1	1	\N	0	0	0	6	0	12	0	0	0	\N	0	0	1	1	1	1	{4}	5	1	0	1	0	2	0	0	0	0	3	2	2	2	1	1	0	2	2	1	1	1	1	1	1	1	2	1	2	1	2	3	1	8	8	8	8	5	2	2	2	2	5	5	0	3	\N	0	11	1	{2,3}	0	12	0	\N	2	7	3	6	0	2	2	0	1	\N	\N	\N	\N	0	0	0	0	0	0	8	1	1	1	0	0	3	0	1	\N	\N	\N	\N	0	\N	3	4	4	2018-11-06	5
170	220	4	1	1	2	3	2	0	1	0	3	2	4	1	3	4	0	1	0	0	4	5	2	1	1	0	1	1	1	7	1	2	6	2	0	1	\N	2	3	0	5	0	2	0	1	0	\N	1	2	1	1	1	1	{4}	4	1	\N	1	0	2	\N	0	0	0	0	\N	5	0	2	1	0	0	4	1	7	0	6	0	1	4	5	1	2	1	1	6	1	2	5	3	1	3	1	6	1	1	8	2	0	5	8	0	\N	1	{2}	0	12	\N	0	2	6	0	5	0	2	2	1	0	3	0	5	0	1	5	1	1	0	0	5	1	6	4	0	0	2	0	1	\N	\N	\N	\N	\N	0	1	0	0	2018-11-08	2
171	219	2	1	4	2	4	2	1	0	1	3	3	4	1	2	3	1	0	0	0	5	5	0	0	1	0	1	1	7	6	0	0	8	0	1	1	\N	2	1	0	1	0	12	0	1	1	\N	2	3	1	0	1	1	{4}	4	0	0	0	4	0	3	3	0	0	0	0	1	0	0	1	0	1	1	1	0	0	6	1	1	1	2	1	3	5	0	5	1	3	4	3	0	1	2	4	1	1	4	2	0	5	9	1	\N	1	{2,3}	1	\N	4	0	2	0	2	6	0	4	3	6	1	\N	\N	\N	\N	0	0	0	0	0	0	5	0	0	0	0	0	3	0	1	\N	\N	\N	\N	5	0	3	2	4	2018-11-06	2
172	222	5	0	0	4	3	2	1	0	4	1	0	4	0	1	4	2	0	0	0	3	5	0	0	\N	0	1	1	0	1	0	7	5	2	1	1	\N	1	0	1	9	2	\N	0	1	1	\N	0	2	0	1	1	1	{3}	7	1	1	1	0	4	4	0	0	0	0	1	3	2	1	1	1	1	3	2	5	3	3	5	3	1	6	0	7	1	2	4	1	3	4	5	7	5	2	8	1	1	2	5	\N	\N	\N	\N	\N	1	{}	\N	\N	0	6	1	7	7	\N	1	1	1	0	1	6	0	\N	2	5	6	1	0	0	0	5	0	0	4	0	0	1	1	0	5	0	0	0	1	0	0	0	0	2018-11-06	2
173	223	4	0	2	1	2	6	1	1	2	3	1	4	1	3	3	1	0	0	0	5	0	0	1	1	3	1	0	0	0	0	0	7	2	1	1	\N	2	0	1	5	1	\N	0	1	0	\N	0	1	0	1	1	1	{0}	7	1	\N	1	4	2	0	0	2	3	3	3	0	7	3	0	1	7	1	1	0	0	8	\N	0	4	3	0	1	1	\N	8	1	8	7	6	6	4	2	1	1	1	7	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	2	1	6	3	6	0	2	1	0	1	\N	\N	\N	\N	\N	\N	1	0	0	1	\N	\N	\N	\N	\N	\N	1	1	1	\N	\N	\N	\N	0	1	1	3	1	2018-11-06	3
174	225	3	1	1	2	4	5	0	0	3	3	2	4	1	3	3	2	0	2	0	0	4	1	0	1	0	1	1	0	0	0	7	5	1	1	1	1	2	1	0	5	0	4	0	0	0	\N	0	1	0	1	1	1	{4}	7	1	1	1	4	4	0	0	0	4	1	2	2	1	0	0	0	2	1	0	0	0	8	0	1	3	4	1	1	0	0	5	0	1	0	3	0	1	2	4	0	0	5	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	0	6	5	6	0	4	6	8	0	7	0	4	2	0	0	0	1	1	0	3	0	0	4	3	1	2	0	1	\N	\N	\N	\N	2	2	4	0	0	2018-11-06	5
175	224	3	0	0	2	2	3	1	0	0	2	3	3	1	2	4	1	3	0	0	5	5	0	0	3	0	1	1	2	2	0	1	1	0	1	0	\N	2	2	0	0	0	2	0	0	1	0	2	1	1	1	1	1	{6}	6	1	\N	1	3	0	3	5	0	0	0	0	0	0	1	0	0	2	4	4	0	0	5	2	2	6	5	0	3	3	3	5	1	5	6	5	5	2	4	4	1	3	4	2	0	1	0	0	13	1	{2}	1	3	5	1	2	6	2	5	0	2	1	4	1	\N	\N	\N	\N	\N	6	1	4	2	0	4	0	0	0	1	0	3	0	1	\N	\N	\N	\N	5	0	1	0	0	2018-11-06	3
176	227	4	0	1	3	3	6	0	0	0	3	2	3	0	2	4	0	0	0	0	5	5	2	2	3	0	1	1	1	1	0	7	8	2	1	1	\N	2	0	0	1	0	4	0	0	0	\N	1	0	2	1	1	1	{4}	5	1	1	1	0	\N	4	2	0	0	0	3	5	2	4	1	1	1	2	3	1	0	6	1	3	1	3	0	0	1	2	8	2	2	4	5	0	5	4	3	1	1	6	3	0	3	8	0	12	0	{2,3}	0	4	5	0	1	6	6	6	1	4	2	1	1	\N	0	0	0	0	6	0	1	1	0	4	0	0	7	0	0	3	0	1	\N	0	0	0	1	0	3	0	1	2018-11-06	7
177	226	3	0	0	2	2	6	0	0	2	3	1	1	1	1	3	0	0	0	0	5	0	4	0	2	0	1	0	0	0	0	7	5	2	1	1	\N	2	2	0	5	1	4	0	1	1	\N	1	1	2	1	1	1	{6}	7	1	\N	1	0	0	3	4	0	0	0	1	2	0	1	6	0	0	2	2	0	0	6	0	0	2	0	0	2	3	6	0	0	3	3	4	0	3	3	2	0	0	4	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	6	6	2	0	3	1	5	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	\N	\N	\N	0	0	2	0	1	\N	\N	\N	\N	\N	0	2	0	0	2018-11-08	3
178	228	4	0	0	2	2	6	0	1	0	3	2	4	1	3	3	1	0	0	0	5	5	3	1	1	0	1	1	0	0	0	0	\N	1	1	1	\N	0	0	1	\N	\N	\N	0	0	1	\N	0	2	0	1	1	1	{0}	7	0	0	1	4	2	0	0	0	3	0	1	0	0	0	0	1	0	0	0	0	0	4	0	0	4	4	0	0	0	1	4	0	0	1	0	0	0	1	2	0	0	2	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	7	5	4	0	4	5	2	1	\N	0	0	0	0	0	1	0	0	1	\N	0	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	1	0	0	2	0	2018-11-06	7
179	229	3	1	4	1	1	6	1	0	0	2	1	4	0	3	3	1	3	0	0	5	5	4	4	2	0	1	1	0	0	0	0	8	1	1	1	\N	2	1	0	9	0	4	0	0	1	\N	1	2	0	1	1	1	{0}	7	1	1	1	5	3	0	0	0	0	1	1	0	0	0	1	0	1	1	3	1	1	6	3	1	3	3	1	6	1	1	3	3	3	3	3	3	2	1	6	1	1	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	1	3	2	7	2	3	0	2	5	4	1	\N	\N	\N	\N	1	\N	0	0	0	0	7	1	2	1	1	0	2	0	1	\N	\N	\N	\N	\N	3	4	0	2	2018-11-08	2
180	230	4	1	0	2	2	3	0	0	2	3	1	3	1	3	2	1	1	0	0	0	0	0	0	1	0	1	0	1	1	0	0	5	2	1	1	\N	2	1	0	0	0	6	0	1	1	\N	2	0	0	1	1	1	{0}	4	0	1	0	0	0	\N	3	0	1	0	7	1	0	0	0	0	0	1	3	1	1	6	0	0	1	5	1	0	0	0	6	0	2	5	2	2	2	3	0	0	0	4	0	0	5	1	0	5	1	{2}	0	6	4	1	2	5	0	\N	0	1	4	1	1	\N	\N	\N	0	0	0	1	0	0	1	\N	\N	0	\N	\N	\N	2	0	1	\N	\N	\N	\N	1	0	0	0	2	2018-11-06	0
181	231	2	0	0	2	4	3	1	0	2	3	4	4	0	4	3	1	0	0	0	3	5	2	4	3	0	1	1	7	0	0	7	5	2	1	1	\N	2	0	1	6	2	6	0	1	0	\N	0	2	0	1	1	1	{4}	\N	1	\N	1	0	2	0	0	0	0	0	1	4	2	5	2	1	1	5	2	3	0	5	1	2	5	5	0	2	2	1	6	1	5	6	5	5	2	3	5	1	1	5	5	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	7	2	6	0	3	4	0	0	6	4	7	\N	3	\N	1	4	0	0	6	1	6	4	1	1	0	0	0	\N	1	0	1	1	0	2	0	0	2018-11-08	2
182	235	3	0	4	4	0	\N	1	0	3	3	3	4	1	1	3	0	0	0	\N	5	5	0	0	1	0	1	1	0	0	0	\N	\N	\N	1	1	\N	3	1	\N	\N	\N	\N	0	1	1	\N	1	3	1	1	1	1	{4}	7	1	1	1	0	2	4	3	0	0	\N	5	5	2	1	0	0	2	2	5	0	0	5	2	2	5	0	1	0	3	2	1	0	0	0	5	0	1	1	3	1	1	2	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	5	5	4	0	4	1	\N	0	7	1	4	2	3	6	0	2	1	0	5	1	6	7	\N	\N	4	0	0	\N	0	0	0	3	0	0	0	1	2018-11-08	\N
183	233	\N	1	0	1	0	0	1	0	3	2	1	4	1	4	3	2	0	0	0	3	5	0	0	1	6	0	1	2	1	0	7	0	1	1	1	\N	1	0	1	9	1	\N	0	0	1	0	2	2	2	1	1	1	{4}	7	1	1	0	4	2	0	0	0	0	1	8	\N	0	0	0	0	1	7	1	1	0	2	0	2	8	2	1	2	1	1	3	3	0	6	7	0	6	2	7	0	1	7	3	\N	\N	\N	\N	\N	1	{}	\N	\N	6	1	2	7	3	0	0	1	3	0	1	\N	\N	\N	\N	1	0	1	4	2	1	\N	\N	\N	\N	\N	\N	4	0	1	\N	\N	\N	\N	5	0	1	0	0	2018-11-06	2
184	234	3	0	3	2	4	5	1	0	2	3	2	2	0	2	4	1	2	0	0	5	1	0	0	2	0	1	1	0	2	0	0	8	2	1	1	\N	2	1	0	6	0	6	0	1	0	\N	0	2	3	1	1	1	{4}	7	1	1	1	0	2	0	0	0	0	0	0	0	0	0	1	0	1	5	5	1	0	8	2	1	7	7	0	1	1	1	8	0	7	6	0	7	7	4	3	1	8	3	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	1	2	2	7	1	1	0	2	8	1	1	\N	\N	\N	\N	0	\N	0	0	0	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	0	1	0	2	2018-11-08	2
185	236	5	0	0	\N	4	6	\N	0	2	3	3	4	0	3	4	0	0	2	0	3	5	\N	2	1	0	0	1	1	3	0	0	\N	1	1	1	\N	2	2	0	0	0	12	0	0	0	\N	1	3	0	1	1	1	{4}	7	1	1	\N	4	4	4	0	0	3	0	0	0	1	0	0	0	0	0	0	0	0	5	2	0	5	2	0	8	2	5	0	5	5	5	5	2	3	6	1	0	1	5	5	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	7	2	6	1	3	1	0	1	\N	\N	\N	\N	2	\N	1	2	4	0	\N	1	5	7	0	0	4	\N	\N	\N	\N	\N	\N	2	0	2	\N	0	2018-11-06	5
186	237	3	0	3	2	2	6	1	0	3	3	2	4	0	3	4	1	0	4	3	5	5	0	0	1	2	1	1	2	0	0	\N	1	0	1	1	\N	2	1	1	0	0	12	0	1	1	\N	1	0	2	1	1	1	{4}	3	1	1	0	0	2	5	0	0	0	1	0	0	0	0	0	0	2	4	1	\N	0	6	0	0	5	5	0	2	0	0	4	6	5	5	\N	6	0	4	5	5	0	1	5	0	\N	\N	\N	\N	0	{}	\N	\N	0	0	2	7	1	0	0	1	1	0	0	0	0	0	0	0	0	0	1	0	1	\N	0	0	0	\N	0	3	0	1	\N	0	0	0	5	0	2	2	1	2018-11-08	0
187	239	2	1	0	3	1	6	0	0	2	3	4	4	0	4	3	1	0	0	0	2	5	\N	0	3	0	1	1	0	0	0	0	9	0	1	1	\N	2	3	0	0	0	6	0	0	1	\N	2	2	1	1	1	1	{3}	\N	0	0	1	3	2	0	0	0	0	0	5	5	0	1	0	0	0	1	5	0	0	6	0	1	1	1	1	0	0	0	1	2	1	5	1	0	5	3	1	0	0	1	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	0	\N	0	0	8	7	0	6	0	0	0	0	0	1	2	1	0	6	2	5	4	2	2	3	0	1	\N	0	0	0	1	\N	2	0	1	2018-11-06	0
188	238	4	0	\N	4	0	\N	0	0	\N	3	4	4	0	4	4	0	1	0	0	5	5	0	0	3	0	1	0	2	1	0	1	\N	1	1	0	\N	\N	0	0	\N	0	\N	0	0	1	0	3	2	2	1	1	1	{4}	4	1	1	\N	0	0	3	0	0	3	0	5	5	2	3	3	0	3	1	5	1	0	6	2	2	0	0	1	0	5	0	7	3	2	5	5	0	3	3	3	1	0	1	3	0	5	5	0	11	1	{1,2,3}	1	\N	4	0	1	0	4	6	0	\N	0	0	0	1	0	6	0	0	0	0	2	0	0	2	0	0	0	0	0	3	0	1	\N	\N	\N	\N	1	1	2	0	0	2018-11-06	4
189	240	3	0	2	4	0	0	0	1	0	0	1	2	0	2	0	0	3	2	3	2	5	0	1	2	2	0	1	4	2	5	4	4	\N	1	1	0	1	4	1	5	1	6	0	0	1	\N	1	1	2	1	0	\N	{3}	6	0	0	0	0	2	0	0	0	3	0	4	4	4	4	4	0	3	7	3	8	3	8	8	8	4	5	1	7	8	8	6	0	4	4	3	4	4	4	8	4	8	4	4	0	3	1	0	5	0	{1}	0	6	7	5	4	4	2	1	1	4	9	8	0	7	6	7	1	2	3	1	3	1	0	7	3	3	2	3	2	4	0	0	6	3	1	0	4	0	0	2	1	2018-11-08	7
190	241	4	0	4	1	4	6	0	3	1	2	1	4	0	2	4	1	2	0	0	4	0	0	1	2	7	\N	1	5	1	0	0	\N	2	0	1	1	2	3	0	0	0	4	0	0	3	\N	4	3	0	0	1	1	{4}	7	1	1	1	4	2	0	4	0	0	0	2	3	1	6	5	0	4	6	5	1	1	6	3	1	1	2	0	0	0	5	3	3	0	5	2	0	1	3	5	1	0	0	5	0	5	1	0	\N	1	{1}	1	13	0	6	2	1	1	3	0	0	1	0	0	3	1	3	1	2	6	0	1	0	0	5	1	2	4	1	4	3	0	1	\N	\N	\N	\N	\N	0	3	0	0	2018-11-06	0
191	242	\N	1	0	2	1	1	1	0	0	3	3	3	1	3	3	1	3	0	0	2	5	1	0	2	\N	1	1	0	2	0	0	\N	2	1	1	\N	1	1	1	\N	\N	\N	0	1	1	1	1	2	3	0	1	0	{2}	\N	1	1	1	2	2	2	5	0	3	2	0	1	2	2	1	0	2	5	5	3	3	6	1	2	3	2	1	2	2	3	2	3	3	6	5	0	3	3	2	2	2	0	1	\N	\N	\N	\N	\N	1	{}	\N	\N	2	1	2	7	5	6	0	4	0	0	1	\N	\N	\N	\N	\N	0	0	0	0	0	7	0	0	0	0	0	1	0	1	\N	0	\N	\N	1	1	3	0	4	2017-11-06	5
192	249	4	1	0	3	1	6	1	1	0	3	3	3	0	3	2	1	2	0	0	3	5	0	4	1	0	1	1	0	0	0	0	\N	1	1	1	\N	0	2	0	0	0	12	0	0	0	\N	1	2	0	1	1	1	{4}	4	1	\N	1	2	1	0	4	0	0	0	3	3	3	3	3	0	2	5	2	1	1	6	3	2	3	2	0	2	2	0	5	1	2	1	3	1	3	5	3	1	1	3	1	0	5	9	1	\N	1	{3}	1	\N	5	1	2	5	2	6	1	2	3	1	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	0	\N	\N	\N	\N	5	0	1	\N	0	0	0	0	0	4	3	4	2018-11-08	2
193	251	4	1	0	3	1	0	0	0	2	3	3	4	0	1	3	2	1	0	0	5	5	3	1	2	0	1	1	1	0	1	\N	5	1	1	1	\N	2	2	0	5	0	4	0	1	1	\N	3	1	2	1	1	1	{6}	3	1	1	1	1	1	0	1	0	0	1	1	0	6	2	1	0	1	2	4	1	1	6	2	1	5	3	1	2	2	0	6	1	4	6	4	3	3	5	5	1	3	4	2	0	1	0	0	\N	1	{2,3}	0	3	6	0	1	3	5	3	0	4	1	0	1	\N	0	\N	0	0	0	0	0	1	0	0	1	1	5	0	0	2	0	1	\N	0	0	0	1	0	3	1	2	2018-11-08	5
288	364	4	0	0	3	1	6	1	0	1	0	4	2	1	4	4	2	2	0	0	5	0	0	0	2	0	1	1	1	0	0	3	5	0	1	1	\N	1	2	0	1	0	6	0	1	2	\N	2	1	2	1	1	1	{0}	3	1	1	1	0	0	0	0	2	4	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	1	\N	6	\N	6	0	3	2	2	1	\N	0	0	0	0	\N	0	0	0	1	0	0	0	0	0	0	1	0	1	\N	0	0	0	0	0	4	0	0	2018-10-02	2
194	252	0	0	2	3	0	6	1	0	1	3	3	3	1	3	3	1	0	0	0	0	0	0	0	1	0	1	1	0	0	0	0	1	1	1	1	\N	3	1	0	\N	0	0	0	0	1	1	0	1	0	1	1	1	{5}	6	1	1	1	2	2	0	4	0	1	0	0	0	1	0	2	0	2	3	1	1	1	7	2	1	2	1	1	2	2	1	7	7	3	3	3	1	3	1	2	2	2	2	2	0	5	9	1	\N	1	{2}	1	\N	0	\N	1	7	3	5	0	2	1	0	1	\N	\N	\N	\N	1	\N	0	1	0	\N	7	\N	\N	\N	\N	\N	5	1	\N	\N	\N	\N	\N	\N	0	3	2	4	2018-11-08	7
195	254	4	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	7	1	1	1	5	0	4	0	0	3	0	2	2	0	2	2	0	2	3	2	0	0	6	2	0	5	2	0	1	1	0	6	1	7	7	1	0	2	3	2	0	0	2	0	0	5	9	1	\N	1	{2,3}	0	12	0	\N	2	6	1	5	0	1	2	0	1	\N	\N	\N	\N	1	0	0	0	0	1	\N	0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-08	1
196	253	4	0	0	3	0	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	7	1	1	1	4	0	0	5	0	0	0	3	3	0	0	1	1	0	2	2	5	0	6	0	0	5	2	1	0	2	0	6	0	5	7	0	0	3	6	0	0	1	0	0	0	5	8	0	13	0	{1,2,3}	1	\N	0	\N	2	7	4	6	0	4	2	0	1	\N	\N	\N	\N	1	0	0	0	0	0	8	0	0	0	0	0	1	0	1	\N	0	0	0	0	0	\N	2	4	2018-11-08	4
197	255	4	1	2	2	1	6	\N	0	2	3	3	2	1	4	5	1	2	0	0	4	5	0	3	1	0	1	1	0	1	1	0	\N	1	1	1	\N	2	\N	0	9	0	6	0	0	0	\N	1	3	1	0	1	1	{4}	1	1	1	1	0	2	4	0	0	1	1	3	3	3	3	\N	0	5	5	1	1	6	5	2	5	3	4	0	1	7	2	2	6	6	6	5	5	6	4	6	3	3	2	0	\N	0	1	1	10	1	{2,3}	0	12	5	6	2	5	5	6	0	3	3	5	0	\N	\N	\N	\N	\N	6	0	0	0	0	5	4	6	7	2	0	3	1	1	\N	\N	\N	\N	2	\N	3	0	0	2018-11-18	0
198	256	3	0	1	4	0	\N	1	1	0	3	4	4	1	4	5	1	0	0	0	5	0	0	0	2	0	1	1	0	0	0	0	\N	0	1	1	\N	0	0	1	10	1	12	0	0	0	\N	0	2	0	1	1	1	{4}	6	1	\N	1	0	2	0	5	0	0	0	6	6	0	0	2	0	2	3	6	2	0	5	5	2	2	5	0	5	6	0	5	0	0	6	6	0	0	2	6	5	2	7	2	0	5	9	1	\N	0	{0}	1	\N	0	0	2	\N	2	6	0	3	0	8	1	\N	\N	\N	\N	\N	\N	0	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	0	4	0	4	2018-11-08	2
199	259	5	0	0	0	0	6	1	1	0	3	0	0	1	0	0	2	0	0	0	0	0	1	0	1	0	0	1	0	0	0	0	9	0	1	\N	\N	1	0	1	10	0	1	1	1	0	1	0	0	0	1	1	1	{3}	1	\N	1	0	0	2	\N	0	0	0	0	0	0	0	2	0	1	0	2	1	0	0	5	2	2	0	1	0	1	2	1	4	0	1	0	1	0	1	5	1	0	1	0	0	1	0	0	1	0	\N	{1,2,3}	1	0	5	1	2	5	2	5	0	2	3	1	0	4	5	0	0	0	0	0	0	0	1	\N	0	0	0	0	0	1	0	1	0	0	0	0	0	0	0	0	0	2018-11-18	4
200	257	4	0	0	0	0	6	1	0	0	3	3	0	0	0	\N	1	3	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	1	0	1	0	1	0	1	\N	1	12	1	1	0	\N	0	1	0	1	1	0	{0}	7	1	1	1	0	2	0	0	0	0	0	5	5	1	1	2	0	1	1	1	1	1	6	6	2	1	2	1	2	1	1	1	1	1	5	5	1	2	2	5	1	1	1	1	0	5	9	1	\N	1	{1,3}	1	\N	5	0	2	5	2	5	0	2	3	2	\N	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	\N	\N	\N	\N	\N	0	1	\N	0	0	0	0	0	0	0	0	2018-11-08	4
201	260	3	1	2	2	0	\N	1	1	1	3	3	4	1	4	5	2	1	0	0	5	5	0	0	\N	0	1	1	0	0	0	0	8	0	1	1	\N	0	4	0	5	0	4	0	\N	1	\N	0	2	1	1	1	1	{6}	\N	1	1	1	0	\N	4	5	0	3	0	0	5	1	1	0	0	0	0	3	0	0	4	1	0	1	3	1	0	0	0	1	1	2	0	1	0	2	2	3	2	2	0	2	0	\N	\N	\N	\N	1	{}	\N	\N	0	5	2	7	1	6	0	1	0	0	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	0	4	5	4	4	0	0	3	0	1	\N	\N	\N	\N	\N	0	4	\N	4	2018-11-08	2
202	262	1	1	\N	\N	1	\N	\N	1	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	1	1	\N	\N	\N	\N	\N	1	1	1	5	1	0	\N	\N	1	\N	0	0	1	\N	1	\N	2	1	1	1	{4}	1	1	1	1	0	0	0	0	0	0	0	5	0	3	2	0	0	0	2	4	0	4	4	0	0	3	\N	1	\N	\N	5	7	0	1	3	\N	\N	\N	3	\N	8	4	4	3	1	1	8	1	5	0	{}	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	0	0	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2004-02-08	\N
203	261	4	0	2	1	3	3	1	1	2	3	2	4	1	4	4	1	0	0	0	4	4	0	4	1	0	1	1	0	0	0	0	9	0	1	1	\N	1	1	0	5	1	6	0	0	0	\N	1	3	0	1	1	0	{6}	5	1	1	0	0	1	3	3	0	0	0	5	5	6	3	3	0	4	4	4	3	3	4	4	7	4	3	0	4	3	6	7	1	4	4	4	4	4	5	3	3	3	4	3	0	5	9	0	\N	1	{1,2,3}	1	13	5	0	2	6	0	0	1	0	3	3	1	\N	\N	\N	\N	0	0	0	1	0	0	4	0	1	3	1	1	3	0	1	\N	\N	\N	\N	1	1	2	1	4	2018-11-08	0
204	263	4	0	1	2	2	6	1	0	2	3	2	2	1	2	4	0	0	0	0	2	5	0	0	2	0	1	1	1	0	0	2	9	0	0	1	2	3	3	0	10	0	3	0	0	2	\N	2	3	1	0	1	1	{5}	6	1	1	0	4	2	5	0	0	0	2	1	1	1	1	1	1	1	5	0	0	1	5	1	2	1	1	1	5	1	0	5	5	5	5	5	0	5	1	5	0	0	5	0	0	5	7	1	\N	1	{1,2}	1	\N	1	1	0	0	0	6	0	1	6	8	0	5	1	3	2	2	9	1	2	1	0	4	1	5	1	4	2	3	0	0	5	2	1	0	2	3	2	0	2	2018-11-08	1
205	266	3	0	0	2	1	6	1	0	0	3	2	4	0	4	3	0	0	0	0	5	4	3	2	2	0	1	1	0	1	0	0	\N	1	1	1	\N	1	0	0	0	0	4	0	1	3	\N	0	2	1	1	1	1	{3}	2	1	1	1	0	0	0	5	0	0	0	3	3	0	1	0	0	3	1	0	1	1	6	1	1	3	3	0	1	1	1	4	3	4	4	4	1	2	3	1	1	1	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	1	0	4	1	2	1	1	1	\N	\N	\N	\N	\N	\N	1	\N	\N	1	\N	\N	\N	\N	\N	\N	3	0	1	\N	\N	\N	\N	\N	0	1	2	1	2018-11-08	0
206	268	4	0	1	4	0	\N	1	1	0	3	2	2	0	2	3	1	1	0	0	2	5	\N	0	1	0	1	1	0	0	0	0	\N	0	1	1	\N	1	0	\N	\N	0	\N	0	0	0	\N	1	2	0	1	1	0	{}	7	1	\N	\N	0	1	0	0	0	1	1	0	8	1	1	0	0	1	3	1	0	0	6	2	2	6	5	0	3	2	0	6	2	0	5	2	0	2	3	3	1	2	2	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	5	2	3	0	2	2	7	1	\N	\N	\N	\N	\N	\N	1	0	0	\N	\N	\N	\N	\N	\N	\N	5	0	\N	\N	\N	\N	\N	\N	\N	\N	1	3	2018-11-08	1
207	264	4	0	2	2	2	6	1	1	2	3	2	2	1	2	4	1	1	0	0	2	0	0	1	2	0	1	1	1	0	0	0	\N	0	1	1	\N	2	1	0	5	0	4	0	0	0	\N	3	2	0	1	1	1	{2,4}	4	1	1	1	3	0	3	3	0	2	0	3	3	1	1	2	0	2	3	1	1	0	6	0	0	1	0	1	0	0	0	1	1	3	5	3	0	3	5	1	1	0	1	0	0	5	9	1	\N	1	{1,2,3}	0	13	0	2	0	0	0	0	0	2	3	2	0	6	0	0	0	2	6	0	1	1	0	6	2	2	4	1	0	3	0	1	\N	\N	\N	\N	1	\N	3	2	1	2018-11-08	0
208	267	4	1	0	1	0	6	1	1	0	3	1	4	1	3	2	0	1	0	0	2	5	0	1	1	0	1	1	0	1	0	0	8	0	1	1	\N	1	2	0	9	0	4	0	0	1	\N	1	2	0	0	1	1	{4}	7	0	1	1	4	2	4	0	0	0	0	0	7	0	2	0	0	6	3	5	0	0	3	5	2	2	2	0	2	2	0	2	0	5	5	5	0	5	3	1	1	0	5	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	7	2	1	1	1	1	0	1	\N	\N	\N	\N	\N	\N	1	0	0	0	7	0	0	7	0	0	3	1	1	\N	\N	\N	\N	\N	0	1	0	3	2003-07-08	2
209	269	1	0	0	4	2	6	1	0	3	2	4	4	0	3	4	0	3	0	3	5	5	4	4	3	2	1	1	0	0	0	1	8	1	1	1	\N	2	2	0	2	0	6	0	0	0	\N	1	2	3	0	1	0	{4}	3	1	1	1	0	2	0	4	0	2	0	0	2	3	0	0	0	1	4	6	2	1	6	5	0	0	4	1	1	2	2	0	1	3	0	4	0	2	2	3	1	0	4	4	0	1	0	1	\N	0	{1}	1	13	0	0	2	0	1	6	0	2	0	0	0	0	0	0	0	0	0	1	4	3	1	0	0	0	0	0	0	1	0	1	\N	0	0	0	0	0	4	2	1	2018-11-08	0
210	270	5	0	0	1	1	6	0	0	2	3	4	4	1	4	5	2	0	0	0	5	5	4	2	2	0	0	0	0	5	0	0	\N	1	1	1	\N	1	0	1	9	0	12	0	1	2	\N	1	1	0	1	1	1	{2}	7	0	0	1	0	2	4	5	0	0	2	2	6	2	1	0	0	1	0	3	3	1	4	3	1	8	7	0	3	3	1	4	1	3	7	6	6	2	3	7	3	6	1	7	\N	\N	\N	\N	\N	0	{}	\N	\N	5	3	2	3	5	5	0	4	1	8	0	4	2	1	2	3	6	0	2	0	0	5	0	0	0	2	1	4	0	0	5	0	0	0	3	0	3	0	1	2018-11-08	7
211	272	5	0	2	4	1	6	0	0	1	3	3	3	1	3	5	2	1	0	0	2	0	3	3	2	0	1	0	0	2	0	0	9	1	1	1	\N	2	1	1	6	0	6	0	0	1	\N	1	3	0	1	1	1	{4}	7	1	1	1	4	2	3	0	0	0	0	2	2	1	5	1	0	2	4	1	0	0	3	3	0	4	4	1	3	2	3	3	0	3	2	3	3	3	3	3	3	1	4	4	0	4	0	1	5	1	{2,3}	0	4	0	1	2	7	2	5	0	3	3	5	0	0	0	5	0	4	6	1	1	0	0	2	2	5	8	1	0	3	0	0	7	1	0	0	3	2	1	4	1	2018-11-08	2
212	271	3	0	0	3	0	\N	1	1	0	3	3	4	1	3	3	1	2	0	0	4	0	0	4	2	0	1	1	0	0	0	2	5	0	1	1	\N	0	2	0	9	0	2	0	1	1	\N	0	2	0	1	1	1	{6}	6	1	1	1	0	0	0	0	0	0	0	6	6	0	1	3	0	2	1	5	0	0	6	1	0	1	0	0	2	1	0	3	0	6	6	3	0	5	3	3	0	3	1	1	0	\N	\N	\N	\N	0	{}	\N	\N	2	2	2	6	0	0	1	1	1	2	1	\N	\N	\N	\N	\N	0	1	0	1	1	\N	0	\N	\N	\N	\N	\N	0	1	\N	0	\N	\N	\N	0	3	0	4	2018-11-08	3
213	273	3	0	0	2	2	\N	1	1	3	3	4	4	0	4	4	1	3	0	0	5	5	0	0	1	0	1	1	0	0	0	0	\N	1	1	1	\N	2	0	0	0	0	6	0	0	2	\N	3	3	1	1	1	1	{4}	4	1	1	0	5	2	4	5	0	3	0	5	5	3	2	0	0	2	6	5	2	1	5	0	0	1	6	1	1	2	0	6	0	5	5	5	0	5	3	5	2	2	5	1	0	5	9	0	0	1	{1,2,3}	0	5	5	3	2	0	1	0	1	0	0	2	1	\N	\N	\N	\N	0	0	1	0	0	0	7	2	6	4	1	0	2	1	1	\N	\N	\N	\N	0	0	0	0	0	2018-11-08	0
214	274	4	0	1	0	0	1	0	0	1	3	4	\N	0	1	0	0	0	2	1	2	1	2	2	1	5	0	1	0	2	2	0	0	0	0	1	0	0	2	\N	1	0	3	1	1	0	\N	0	0	0	0	0	0	{2}	5	1	1	1	1	2	0	0	0	0	0	1	3	4	3	0	0	3	3	3	3	2	8	3	3	\N	\N	1	\N	\N	5	\N	4	3	4	\N	\N	\N	2	\N	\N	4	4	4	0	5	2	0	4	1	{1}	0	2	5	1	1	0	0	4	0	2	2	2	0	\N	\N	0	0	\N	6	0	\N	1	0	7	1	1	1	1	1	1	0	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-08	2
215	275	5	1	1	2	2	1	\N	1	4	1	0	3	0	3	\N	1	1	0	2	1	3	4	4	2	0	0	0	7	\N	1	1	0	0	\N	1	1	0	3	0	1	0	0	0	\N	0	\N	1	2	1	0	1	1	{1}	4	1	1	1	0	0	4	4	0	0	0	6	5	6	0	0	0	2	1	2	0	0	6	1	1	1	2	1	3	0	0	5	1	\N	0	4	0	3	3	4	1	0	2	0	0	5	1	0	\N	1	{1,2,3}	0	\N	5	0	2	3	2	5	0	2	2	8	1	\N	\N	\N	\N	1	\N	0	0	0	1	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	0	0	0	0	1	2	0	0	2018-11-08	2
216	276	4	0	0	3	0	\N	1	1	1	3	4	4	1	2	4	2	2	0	0	4	0	0	0	3	0	1	1	0	0	0	0	\N	0	1	0	\N	0	0	0	1	2	\N	0	\N	1	1	1	1	0	1	1	1	{2}	6	1	\N	1	0	0	0	0	0	0	0	3	4	0	4	3	0	1	2	4	0	1	5	1	0	1	1	0	1	1	0	1	2	6	6	5	0	7	4	1	1	1	0	1	0	0	\N	0	11	1	{2}	0	13	0	\N	6	6	3	4	0	3	0	1	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	0	0	1	\N	\N	\N	\N	0	0	2	1	0	2018-11-08	1
217	277	4	0	2	0	2	1	1	0	1	2	3	\N	1	3	4	2	1	0	0	5	5	0	2	1	2	1	1	0	0	0	0	\N	0	1	1	\N	1	2	0	9	0	4	\N	0	0	\N	1	1	2	0	1	1	{3,4,5}	6	1	1	1	0	2	0	0	0	0	0	1	3	1	3	1	0	3	3	2	3	\N	1	3	3	3	\N	1	0	4	3	3	\N	3	0	0	1	4	3	3	3	1	3	1	0	1	8	1	\N	1	{2,3}	\N	1	0	2	0	1	0	0	1	1	2	0	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	0	0	2	0	1	\N	\N	0	0	0	0	0	2	2	2018-11-08	1
218	279	4	0	0	4	0	\N	1	1	0	3	1	4	1	1	5	1	0	0	0	3	5	0	4	1	0	1	1	0	0	0	0	1	1	1	1	\N	1	1	1	9	0	6	0	0	0	\N	1	2	0	1	1	1	{4}	7	1	1	1	4	0	4	0	0	0	0	0	8	1	2	3	0	1	2	0	0	0	8	0	0	7	5	0	0	1	1	8	0	4	8	8	0	8	4	1	0	1	8	1	0	5	1	0	9	1	{}	1	\N	2	0	2	7	2	0	0	1	9	0	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	0	\N	\N	\N	\N	\N	\N	0	0	1	\N	\N	\N	\N	0	0	4	0	2	2018-11-08	0
219	280	1	1	0	1	3	6	1	0	3	3	3	4	0	4	2	0	1	0	0	\N	0	1	0	1	0	1	1	1	0	0	7	\N	1	1	1	1	\N	1	1	0	0	5	0	0	1	\N	1	1	3	1	1	1	{5}	7	1	1	0	0	0	4	0	0	0	1	0	0	6	\N	0	0	0	0	2	3	0	0	4	2	2	3	0	1	0	0	2	3	2	8	4	4	4	3	2	0	3	4	2	0	3	8	0	2	1	{1,2}	1	12	2	0	2	4	2	0	0	1	6	\N	1	\N	0	0	0	0	0	1	0	0	0	7	\N	\N	0	0	0	1	0	1	0	0	0	1	1	1	1	3	1	2018-11-08	0
220	278	1	0	1	1	2	3	1	0	0	3	\N	4	1	4	5	1	3	0	0	0	0	0	0	2	0	1	1	0	0	0	0	9	0	0	1	\N	2	3	0	0	0	\N	0	0	1	1	1	2	0	1	\N	\N	{4,5,6}	4	1	1	1	5	2	4	3	0	3	0	6	1	0	1	1	0	1	2	1	1	1	1	1	1	1	1	1	0	1	1	1	6	4	3	7	1	3	2	3	1	3	3	1	0	5	1	0	10	0	{2,3}	0	11	0	0	2	2	1	3	0	1	3	1	1	\N	0	0	0	0	0	1	0	1	1	\N	0	0	0	0	0	2	0	1	\N	0	0	0	\N	0	2	0	2	2018-11-08	1
221	281	5	0	0	0	1	0	1	\N	4	2	3	4	0	2	3	0	3	2	3	0	5	2	0	1	0	1	1	0	0	0	2	8	1	1	1	\N	3	3	0	6	0	4	0	1	1	0	1	2	0	0	1	1	{4}	1	1	1	1	5	2	5	5	0	0	1	0	0	1	3	0	0	0	3	0	0	0	1	0	3	0	0	0	4	2	1	0	0	3	0	\N	\N	\N	3	\N	\N	0	0	0	0	5	2	1	\N	1	{2,3}	1	\N	5	1	2	0	0	0	0	1	0	8	1	\N	0	0	0	0	0	0	0	0	0	6	1	6	7	1	0	3	0	1	\N	0	\N	\N	\N	\N	3	3	3	2018-11-08	0
223	282	1	1	0	4	0	\N	0	0	1	3	2	4	0	4	5	1	0	0	0	0	5	0	1	2	0	1	1	0	0	0	0	\N	0	1	1	\N	2	1	1	0	0	6	0	0	0	\N	0	2	0	1	1	1	{4,5,6}	1	1	1	1	4	2	0	0	0	0	0	5	\N	0	5	0	0	5	0	0	0	0	4	0	3	3	3	1	1	0	0	4	6	0	8	0	2	3	2	0	0	3	2	0	1	1	2	0	6	1	{1}	0	1	0	5	4	0	2	6	0	0	7	7	1	\N	\N	\N	\N	\N	\N	0	0	0	0	7	3	6	7	1	\N	2	0	1	\N	\N	\N	\N	\N	0	4	0	1	2018-11-08	1
222	283	0	1	0	0	0	\N	\N	\N	2	0	0	0	0	0	\N	1	\N	\N	\N	\N	\N	\N	\N	1	\N	1	1	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	1	1	\N	0	\N	\N	\N	1	1	1	{0}	0	1	0	0	0	\N	0	0	2	0	0	0	0	0	0	0	\N	0	0	0	0	0	0	0	3	0	0	0	0	0	\N	1	1	0	0	0	1	8	4	8	4	0	0	8	0	1	1	1	0	1	{1}	1	0	0	6	0	1	1	1	0	0	9	0	1	\N	\N	\N	\N	0	6	0	\N	0	0	8	1	0	0	4	0	4	0	1	\N	0	\N	1	0	0	0	0	0	2018-11-08	1
224	285	3	1	0	0	0	\N	1	1	2	1	2	4	0	4	4	0	1	0	0	1	4	4	1	2	0	1	1	0	0	0	0	\N	0	1	1	\N	2	0	0	0	0	12	0	0	0	\N	1	1	2	1	1	1	{0}	1	1	1	0	0	2	0	4	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	8	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	6	\N	1	\N	3	0	4	5	2	1	\N	\N	\N	\N	\N	\N	1	2	0	0	7	1	1	1	0	0	1	1	1	\N	\N	\N	\N	0	0	1	0	0	2018-09-14	2
225	284	4	0	1	3	0	5	0	1	0	2	4	4	0	4	5	1	1	0	0	2	2	2	1	1	0	1	0	1	1	0	0	\N	2	1	1	\N	0	0	0	6	0	4	0	0	1	\N	1	2	3	1	0	1	{3}	7	1	1	0	0	2	4	0	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	6	\N	4	\N	5	0	3	1	4	1	\N	0	\N	\N	\N	\N	0	1	0	1	\N	\N	0	0	0	0	2	1	1	\N	\N	0	0	5	0	1	2	2	2018-09-14	2
226	287	4	1	4	4	1	5	1	1	2	0	2	4	1	1	5	2	2	0	1	1	5	0	0	1	0	0	0	0	0	4	3	4	2	1	1	\N	4	4	0	1	0	4	0	1	0	\N	0	2	0	1	1	1	{0}	0	1	1	0	5	2	5	5	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	2	\N	0	0	0	6	8	0	2	0	0	2	0	1	1	4	0	0	0	2	6	8	2	0	4	1	1	\N	\N	\N	\N	\N	1	0	0	2	2018-09-14	0
227	286	4	1	3	1	4	0	0	2	4	2	4	4	0	4	1	2	2	2	2	2	5	4	2	0	0	1	1	3	0	\N	0	0	\N	1	1	\N	1	1	0	0	1	12	0	0	1	1	3	3	1	1	1	1	{4}	1	0	0	0	2	2	3	0	0	\N	3	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	2	1	1	3	\N	\N	3	\N	1	0	1	8	1	1	\N	\N	\N	1	{}	\N	\N	\N	\N	\N	\N	\N	\N	0	1	7	1	0	9	0	0	0	0	\N	\N	4	1	0	7	2	1	2	0	3	1	0	0	\N	\N	\N	\N	1	1	2	4	2	2018-09-14	\N
228	289	4	\N	0	4	2	3	1	0	1	3	4	4	1	4	5	0	1	0	0	0	5	4	1	2	0	1	1	0	0	0	0	\N	0	1	1	\N	1	0	0	8	1	6	0	1	0	\N	0	1	1	1	1	1	{2,6}	7	1	1	0	0	2	0	0	0	1	4	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	\N	\N	1	6	5	6	1	6	1	4	1	1	0	9	1	1	2	2	\N	1	3	1	0	6	1	2	2	0	0	4	1	1	\N	0	0	0	1	0	4	2	4	2018-09-14	3
229	288	3	1	2	4	2	6	0	0	1	2	4	4	1	4	4	1	2	0	1	1	3	4	3	1	0	1	1	2	0	2	2	1	0	1	1	\N	1	1	0	0	0	5	0	0	0	\N	0	1	0	1	1	1	{4}	7	1	1	1	0	3	0	0	0	0	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	6	\N	\N	\N	3	0	2	0	0	1	\N	\N	\N	\N	\N	\N	1	\N	0	0	5	1	1	7	0	0	5	1	1	\N	\N	\N	\N	5	1	1	4	4	2000-02-23	3
230	290	2	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	2	1	0	\N	2	1	0	6	1	6	1	0	0	0	1	2	3	1	1	1	{0}	3	1	1	0	0	\N	0	0	0	3	2	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	\N	\N	\N	1	0	1	9	1	0	\N	1	4	\N	1	0	1	0	0	\N	0	0	3	\N	\N	1	0	0	1	11	\N	\N	\N	1	3	\N	4	3	2018-09-14	1
231	291	4	0	1	0	0	6	1	1	2	3	4	4	0	3	5	1	3	5	5	3	5	0	0	2	0	1	1	0	0	0	0	9	0	1	0	\N	0	0	0	0	1	4	0	1	0	\N	0	1	3	1	1	1	{0,3,5}	7	1	1	0	0	2	0	0	0	0	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	3	1	0	2	2	2	0	3	5	8	1	\N	\N	\N	\N	\N	\N	1	3	4	1	\N	0	0	0	0	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	4	4	1	2018-09-14	3
232	293	4	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	{}	0	0	0	0	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-09-14	\N
233	292	1	1	1	4	2	2	0	1	2	1	0	4	1	4	2	1	0	0	0	0	5	0	0	0	0	1	1	0	0	0	0	9	\N	1	1	\N	1	1	0	6	\N	6	0	0	0	\N	1	1	0	1	1	1	{3}	7	1	1	1	0	2	0	2	0	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	2	6	\N	\N	\N	1	1	0	1	0	0	9	1	0	0	0	\N	1	0	1	0	7	0	0	7	1	0	3	1	1	\N	0	0	0	2	1	4	2	0	2018-09-14	1
234	296	0	1	0	4	3	1	1	0	2	3	2	3	0	3	4	0	3	1	2	0	5	0	0	1	1	1	1	1	0	1	5	9	2	1	1	\N	1	1	1	6	0	4	1	0	0	\N	0	2	3	0	1	1	{3}	1	1	1	0	0	2	3	0	0	0	0	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	4	1	\N	\N	4	1	1	1	0	1	1	\N	0	0	0	0	\N	1	3	\N	1	\N	0	0	0	0	0	0	1	1	\N	\N	\N	\N	\N	1	3	0	2	2018-09-14	1
235	294	4	1	0	4	0	6	1	1	1	3	3	3	0	4	1	0	0	0	0	5	2	0	0	2	1	1	0	0	0	0	7	\N	0	1	1	4	1	0	1	10	1	1	1	1	1	\N	1	1	0	1	1	1	{4}	2	1	1	0	4	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	6	0	7	0	3	0	4	3	2	1	1	1	4	0	\N	\N	0	1	0	0	7	0	0	0	0	0	1	0	1	\N	\N	\N	\N	0	0	4	3	2	2818-09-15	\N
236	295	5	1	2	2	0	6	1	1	0	3	4	4	0	4	5	1	3	0	0	5	5	4	0	2	0	1	1	0	0	0	0	\N	0	1	1	\N	1	0	0	0	0	12	0	0	0	\N	0	2	3	1	1	1	{3}	7	1	1	0	0	4	0	3	0	4	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	4	1	\N	\N	6	0	4	1	0	1	\N	0	0	0	0	\N	1	0	0	1	\N	0	0	0	0	0	5	0	1	\N	0	0	0	0	0	4	4	4	2018-09-14	6
237	299	4	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	6	1	1	1	1	4	0	5	1	0	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-09-14	\N
238	297	5	1	2	2	0	6	0	1	4	3	2	4	0	2	4	0	3	0	0	2	1	0	4	1	2	1	1	3	3	1	2	1	1	0	1	4	2	0	0	0	0	4	0	0	0	\N	1	2	1	1	0	0	{4}	0	1	1	1	4	2	4	5	0	4	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	0	1	2	6	0	4	5	1	0	4	1	6	1	6	9	1	4	0	0	5	1	6	7	1	0	3	0	0	4	4	1	0	3	4	0	2	0	2004-09-14	1
243	303	3	1	0	3	1	0	1	0	2	3	2	4	0	4	5	1	2	0	5	3	4	1	3	0	3	0	1	1	2	0	\N	\N	\N	1	1	\N	2	2	0	0	0	6	0	0	0	1	0	2	3	\N	\N	\N	{0,3,6}	0	0	\N	0	0	1	5	5	2	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	2	7	6	6	0	2	2	7	1	11	4	\N	1	2	4	1	0	2	0	1	5	5	7	4	1	3	0	1	\N	0	0	0	2	1	\N	2	0	2018-09-14	1
244	305	4	1	1	3	3	6	1	0	3	2	4	4	1	4	5	0	2	0	0	4	4	0	0	0	1	1	1	1	0	0	7	5	0	1	1	\N	0	2	0	6	0	4	0	\N	1	\N	0	2	2	1	1	1	{0,3,4,5}	1	1	1	0	3	\N	0	4	0	4	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	2	5	6	4	\N	4	0	4	0	0	0	11	0	7	1	0	\N	1	1	3	0	11	1	2	8	1	0	2	0	1	\N	0	0	0	5	1	1	3	4	2018-09-14	6
245	304	5	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	7	1	1	0	0	4	5	5	1	4	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-09-15	\N
246	336	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-23	\N
247	337	4	0	1	2	1	\N	1	1	2	3	2	4	1	3	5	1	3	0	0	3	0	0	3	2	0	1	1	0	0	0	0	\N	0	1	1	\N	0	2	1	9	1	\N	0	1	0	\N	1	2	1	1	1	1	{4}	4	1	1	1	3	0	0	0	0	3	0	5	2	1	0	0	0	3	7	0	8	0	4	2	0	0	1	0	1	3	0	5	1	2	8	2	0	2	4	4	1	2	3	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	2	6	0	3	0	5	1	\N	\N	\N	\N	\N	0	1	1	0	0	0	1	1	6	0	0	3	0	1	\N	0	\N	\N	0	0	1	0	0	2018-11-23	2
248	338	3	0	0	3	0	\N	1	0	0	3	1	3	1	4	4	1	0	0	0	5	0	0	0	2	0	1	1	0	0	0	1	1	0	1	1	\N	1	0	1	1	\N	\N	0	0	2	\N	1	1	0	1	1	1	{3}	5	1	\N	1	4	3	0	3	1	0	0	5	0	0	0	1	0	1	4	3	0	0	5	1	0	2	1	0	3	1	1	4	0	2	2	3	0	1	2	2	1	3	2	0	0	\N	\N	\N	\N	0	{}	\N	\N	0	\N	1	6	0	\N	0	0	4	8	1	\N	\N	\N	\N	0	0	0	0	0	0	3	0	0	0	0	0	3	0	1	\N	\N	\N	\N	0	0	4	0	2	2018-11-14	0
249	339	4	0	0	2	0	\N	1	1	1	1	2	2	\N	4	3	1	1	0	0	4	0	0	0	3	0	1	1	0	0	0	0	7	2	1	1	\N	2	3	0	1	0	12	0	1	2	\N	1	3	0	1	1	1	{0,6}	4	1	\N	1	3	2	0	3	0	1	0	0	5	1	0	4	0	0	3	3	3	1	6	1	0	5	5	0	1	1	0	3	1	3	6	1	0	1	9	4	0	1	3	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	5	0	\N	0	1	1	7	1	\N	\N	\N	0	0	0	0	0	0	1	\N	0	\N	\N	0	0	1	0	1	\N	0	0	0	0	0	3	1	0	2018-11-23	0
250	343	4	1	1	0	1	0	0	0	1	3	4	4	0	3	5	0	0	0	0	5	5	3	0	2	1	1	1	2	1	0	7	8	2	1	1	\N	1	1	0	6	0	4	0	0	1	\N	0	2	3	1	1	1	{4}	5	1	1	1	0	1	0	0	1	0	0	6	0	0	1	1	1	0	1	1	0	2	6	0	0	6	6	1	0	3	0	5	1	0	4	7	0	4	3	3	1	1	4	3	\N	\N	\N	\N	\N	0	{}	\N	\N	7	0	2	5	7	6	0	4	4	4	1	\N	\N	\N	\N	0	0	0	1	0	0	6	0	1	0	0	0	3	0	1	\N	\N	\N	\N	2	0	4	0	0	2018-11-23	7
251	341	3	0	0	2	0	\N	\N	1	0	3	4	4	1	3	4	1	1	0	0	1	0	0	0	3	0	1	1	0	0	0	0	\N	1	1	1	\N	0	0	1	\N	2	12	1	\N	1	\N	1	2	0	1	1	1	{2}	7	1	1	1	0	0	0	0	1	4	0	6	0	0	3	4	0	4	4	6	1	0	6	3	0	3	6	1	4	4	3	6	3	1	1	6	0	3	5	4	1	3	3	3	\N	\N	\N	\N	\N	0	{}	\N	\N	0	4	0	0	0	0	1	0	0	6	1	\N	\N	\N	\N	0	0	0	0	1	1	0	0	0	0	0	0	1	0	\N	\N	0	0	0	0	0	4	2	1	2018-11-23	0
252	342	5	1	2	0	\N	1	1	0	3	2	1	3	1	3	3	1	1	0	0	4	5	2	1	\N	0	1	1	0	0	0	0	\N	1	1	1	\N	2	4	0	6	0	4	0	0	3	0	3	3	1	1	1	1	{4}	\N	0	0	1	4	2	4	0	0	3	0	1	2	1	1	0	0	0	1	2	0	0	3	1	1	2	1	1	1	1	1	3	2	1	2	5	0	1	4	3	0	1	2	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	0	5	2	0	2	0	4	0	6	0	4	2	3	2	1	4	3	0	5	1	3	4	0	0	3	1	0	6	0	0	0	2	0	3	2	1	2018-11-23	0
253	319	4	0	1	1	2	6	1	0	1	3	4	4	0	3	3	0	0	0	0	0	5	2	0	2	0	1	1	0	1	0	7	7	2	1	1	\N	1	1	0	6	1	0	0	0	0	\N	0	2	0	1	1	1	{4}	4	0	\N	1	0	2	0	4	0	0	1	2	5	4	0	0	0	1	3	3	0	2	6	1	0	1	0	0	3	4	0	5	1	1	6	1	1	2	\N	3	1	1	3	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	4	1	2	6	1	0	2	0	1	1	\N	\N	\N	\N	\N	\N	0	\N	0	0	6	0	0	0	0	0	5	0	1	\N	0	0	0	5	0	4	2	1	2018-11-14	0
255	345	4	0	1	2	0	\N	1	0	2	3	4	4	1	4	3	1	1	0	3	3	0	1	0	2	0	1	1	0	0	0	0	\N	1	1	1	\N	1	0	0	0	0	2	0	1	2	\N	3	3	1	1	1	1	{4}	6	1	\N	0	0	2	0	3	0	4	2	3	3	3	2	0	0	2	0	3	2	0	5	2	2	3	2	0	1	2	0	3	3	3	3	6	3	6	4	2	2	2	0	3	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	1	3	1	0	3	0	1	1	\N	\N	\N	\N	0	0	0	1	0	0	6	0	0	0	0	1	3	0	1	\N	\N	\N	\N	2	0	3	4	4	2018-11-14	1
256	346	5	0	1	2	2	6	1	3	1	0	4	4	1	3	3	1	3	0	0	5	5	0	2	3	1	1	1	3	1	0	7	2	1	1	1	\N	1	1	0	5	0	4	0	0	1	\N	1	3	1	1	1	\N	{4}	2	1	\N	1	4	2	0	4	0	3	0	3	3	0	1	3	0	1	2	3	0	0	4	1	1	2	2	0	1	2	0	3	1	0	3	0	0	1	4	2	1	1	3	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	5	3	1	0	2	2	2	1	\N	\N	\N	\N	\N	0	1	0	0	0	\N	\N	\N	\N	\N	\N	2	1	1	\N	\N	\N	\N	\N	0	3	0	1	2018-11-23	0
257	347	4	1	0	1	0	\N	1	1	0	3	1	4	0	4	4	1	0	0	0	5	5	0	2	2	0	1	1	0	0	0	7	9	0	1	1	\N	0	0	0	0	0	6	0	0	0	\N	0	1	0	1	1	1	{0,2,6}	3	1	1	1	5	2	0	0	0	1	0	1	1	0	0	1	0	0	2	2	0	0	6	1	0	2	3	1	2	3	0	6	1	5	6	2	0	1	3	3	1	1	6	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	6	2	6	0	4	9	8	1	\N	\N	\N	\N	0	0	0	0	0	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	5	0	3	0	4	2018-11-23	2
258	308	4	0	1	3	2	6	1	1	1	3	2	4	1	4	4	1	0	0	0	4	0	0	0	2	0	1	1	0	0	0	0	5	1	1	1	\N	1	1	0	7	0	12	0	1	1	\N	1	2	3	1	1	1	{0,2,6}	4	0	0	1	0	2	0	4	0	2	0	4	4	3	0	3	0	1	1	1	0	0	6	2	1	0	0	0	5	1	1	5	0	3	5	0	0	3	2	3	1	1	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	2	5	2	6	0	2	0	4	1	\N	0	0	0	0	0	0	0	0	1	\N	0	0	0	0	0	1	0	1	\N	0	0	0	0	0	3	1	4	2018-11-23	3
260	328	4	1	1	2	0	\N	1	1	0	3	4	4	1	4	3	2	3	0	0	5	0	0	0	3	0	1	1	0	0	0	0	5	1	1	1	\N	0	1	0	2	0	6	0	0	1	\N	1	3	1	1	1	1	{2,6}	6	1	1	1	0	0	0	4	0	0	0	5	0	1	2	2	0	3	2	1	0	2	1	1	1	2	1	0	1	1	0	3	1	3	5	3	1	3	4	1	1	1	2	1	0	5	\N	\N	\N	0	{}	\N	\N	0	1	2	5	2	6	1	3	2	2	1	\N	0	0	0	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	5	0	1	\N	\N	\N	\N	\N	0	2	0	0	2018-11-23	1
261	335	3	0	0	3	1	0	0	0	0	2	2	3	0	2	4	1	2	0	0	4	5	4	0	2	0	1	1	0	0	0	0	5	2	1	1	\N	0	1	0	0	0	12	0	0	0	\N	3	3	3	1	1	1	{0,3,5}	4	1	\N	1	2	2	4	0	0	1	0	0	6	3	6	4	0	3	3	4	5	0	6	4	4	2	4	0	4	4	4	6	2	5	0	2	0	4	4	4	2	2	6	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	5	7	3	0	4	1	6	1	\N	\N	\N	\N	2	6	0	1	0	0	8	0	0	4	0	0	1	0	1	\N	0	\N	\N	0	1	1	0	1	2018-11-23	7
262	333	4	0	1	2	2	6	1	1	2	3	4	4	1	4	5	1	3	0	0	4	5	0	0	3	0	1	1	0	0	0	1	5	1	1	0	\N	1	3	0	1	0	6	0	0	1	0	1	1	0	1	1	\N	{0}	6	1	\N	1	0	0	0	4	0	0	0	6	3	3	5	6	0	3	1	1	1	0	3	1	1	3	1	0	2	1	1	6	1	2	5	6	0	6	3	0	2	2	3	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	2	2	5	4	6	0	3	1	6	1	\N	\N	\N	\N	0	0	0	0	0	0	5	0	0	0	0	0	2	0	1	\N	\N	\N	\N	\N	0	4	2	3	2018-11-23	2
263	349	4	0	1	1	3	6	0	0	0	3	3	4	1	4	3	2	0	0	0	5	0	0	2	3	0	1	1	2	4	0	0	8	2	1	1	\N	1	3	0	6	0	4	0	0	1	\N	1	2	1	1	1	1	{0,2,3,4}	5	1	1	1	0	0	0	0	0	1	0	6	6	1	6	7	0	1	1	6	1	0	6	3	1	2	6	0	2	6	1	6	2	5	2	8	1	4	5	2	1	1	5	3	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	6	2	1	1	2	9	8	1	\N	\N	\N	\N	0	0	0	2	0	0	0	3	1	4	0	0	2	1	1	\N	\N	\N	\N	0	0	3	1	1	2018-11-23	0
264	309	4	0	4	2	1	3	1	0	3	2	2	4	1	2	3	1	2	0	0	5	5	0	0	1	0	1	1	0	0	0	0	8	1	1	1	1	1	1	0	7	0	12	0	0	1	\N	3	3	3	1	1	1	{4,5}	4	1	\N	1	2	0	0	2	0	1	0	1	1	0	1	3	0	1	5	2	1	0	6	1	1	5	3	0	1	1	1	6	3	3	5	5	0	5	3	1	1	1	1	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	5	3	6	0	3	1	0	1	\N	\N	\N	\N	0	0	1	0	0	1	\N	\N	\N	\N	\N	\N	5	0	1	\N	\N	\N	\N	5	0	3	1	2	2018-11-23	3
266	320	4	0	0	2	3	6	1	1	0	1	4	4	0	2	3	1	2	0	0	5	5	4	2	1	0	1	1	0	0	0	0	8	1	1	1	\N	0	1	0	5	0	4	0	1	0	\N	0	2	0	1	0	1	{0,3,4,5}	6	0	0	1	0	2	0	1	0	0	1	1	1	0	0	0	1	0	1	6	0	0	1	1	0	1	1	0	1	1	0	7	1	0	4	1	0	0	1	3	1	3	1	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	2	5	3	1	0	2	0	2	1	\N	\N	\N	\N	0	0	0	1	1	1	\N	0	0	0	0	1	1	0	1	\N	0	0	0	0	0	4	1	4	2018-11-23	0
267	352	3	0	1	0	2	6	1	0	1	0	1	3	0	2	4	0	0	0	0	2	5	0	0	2	1	1	1	1	0	0	0	4	0	1	1	\N	2	0	1	10	2	\N	0	0	3	\N	2	3	0	1	1	1	{0,4}	6	1	1	1	4	2	4	0	1	4	1	6	6	0	0	0	0	1	1	0	0	0	6	0	1	1	1	0	0	0	0	1	1	1	5	0	0	1	4	0	0	1	2	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	6	1	5	0	6	0	2	0	0	1	\N	\N	\N	\N	0	0	0	0	4	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	5	0	1	0	0	2018-11-23	0
268	353	4	0	0	3	2	6	1	0	2	2	3	4	1	4	5	1	2	0	0	5	0	2	0	1	0	1	1	0	0	0	7	8	1	1	1	\N	1	3	0	0	0	2	0	0	0	\N	2	0	0	1	1	1	{4,5}	3	1	1	1	0	0	0	0	0	0	0	6	6	0	1	4	0	1	1	3	1	0	6	1	1	6	1	0	1	2	2	6	1	6	6	5	0	5	3	1	1	1	1	1	\N	\N	\N	\N	\N	0	{}	\N	\N	5	1	2	5	0	6	0	3	3	3	1	\N	\N	\N	\N	0	0	0	0	1	1	\N	0	0	0	0	0	1	0	1	\N	\N	\N	\N	\N	0	4	0	4	2018-11-23	0
269	327	4	0	0	3	2	6	1	0	2	0	4	4	0	4	5	1	3	0	0	4	0	0	0	3	0	1	1	0	0	0	0	8	0	1	1	\N	1	0	0	10	0	\N	0	1	3	\N	2	1	0	0	1	1	{2,5}	6	1	\N	1	0	0	0	3	0	0	0	0	5	0	3	0	0	1	1	2	0	0	1	1	1	2	0	0	0	0	1	8	1	0	5	2	0	7	3	0	1	1	2	5	\N	\N	\N	\N	\N	0	{}	\N	\N	1	1	2	0	0	0	1	0	0	0	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	0	1	0	1	\N	\N	\N	\N	0	0	3	1	2	2018-11-23	0
265	350	1	0	0	0	4	2	1	0	3	2	4	2	0	0	2	1	1	0	0	5	5	0	0	2	4	1	1	4	0	0	0	8	0	1	1	\N	1	1	1	\N	\N	\N	0	0	2	\N	4	4	0	1	1	1	{6}	7	1	\N	1	5	2	4	0	0	0	0	0	2	2	2	0	1	1	1	1	0	0	2	3	0	1	2	0	1	3	0	3	0	0	1	0	0	3	9	7	0	0	2	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	0	\N	0	1	0	7	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	4	0	1	\N	\N	\N	\N	4	0	3	0	0	2018-11-23	0
270	315	4	0	0	2	2	6	1	0	3	2	4	4	0	4	4	1	2	0	0	3	5	0	0	1	0	1	1	0	0	0	2	9	1	1	1	\N	1	3	0	3	0	12	0	0	0	\N	1	1	1	1	1	1	{6}	6	0	0	1	4	2	0	4	0	4	0	5	5	2	3	3	0	3	3	3	3	2	3	3	3	2	2	1	4	4	4	4	3	4	2	4	4	7	4	2	4	4	4	3	\N	\N	\N	\N	\N	0	{}	\N	\N	3	0	1	5	6	6	0	4	4	3	0	6	0	0	0	0	0	0	1	0	0	6	2	2	6	0	\N	3	0	1	\N	\N	\N	\N	0	0	4	1	1	2018-11-23	6
271	354	5	0	0	4	0	\N	1	1	0	3	1	4	0	3	4	1	3	0	0	5	5	4	0	2	0	1	1	0	0	0	0	5	1	1	1	\N	0	1	0	0	0	6	0	0	1	\N	0	2	0	0	1	0	{0}	6	1	\N	1	4	4	0	0	0	0	0	3	6	1	1	1	0	1	1	6	1	1	6	1	3	2	3	0	4	0	3	6	1	6	5	6	1	1	4	6	0	4	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	5	5	6	1	4	4	2	\N	1	\N	\N	\N	0	\N	1	0	0	1	\N	\N	\N	\N	\N	1	2	0	\N	\N	\N	\N	\N	0	0	4	0	3	2018-11-23	5
273	313	4	0	0	3	0	\N	1	0	0	3	4	2	1	4	3	1	3	0	0	3	0	4	0	1	\N	1	0	0	0	0	0	\N	1	1	1	\N	0	0	1	1	1	\N	0	0	1	\N	1	3	1	1	1	1	{3}	6	1	1	1	3	0	0	0	0	3	0	7	7	3	3	3	0	1	5	3	3	3	6	1	1	6	1	0	1	6	0	0	6	6	6	6	0	7	3	0	1	3	8	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	1	5	4	6	0	4	2	4	1	\N	\N	\N	\N	0	0	0	0	0	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	0	0	4	1	4	2018-11-23	4
274	355	1	0	0	4	0	\N	1	1	2	3	\N	4	0	4	4	1	3	0	5	5	5	0	0	2	0	1	1	0	0	0	\N	\N	0	1	1	\N	0	0	0	0	0	6	0	1	1	\N	1	1	0	1	1	1	{4}	7	1	1	1	4	2	0	0	1	0	0	4	0	3	3	3	0	3	3	3	3	3	7	1	1	3	5	0	0	2	3	0	1	4	4	4	0	3	3	6	1	1	3	3	0	\N	\N	\N	\N	1	{}	\N	\N	0	0	2	0	3	4	0	4	3	4	1	\N	\N	\N	\N	0	\N	0	\N	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	0	4	1	1	2018-11-14	0
275	329	4	0	1	4	0	\N	0	1	1	3	4	4	1	3	3	1	1	0	0	4	0	0	4	2	0	1	1	0	0	0	0	\N	1	1	1	\N	0	1	0	6	0	4	0	0	1	\N	1	1	0	1	1	1	{0}	5	1	1	1	2	0	0	5	0	1	0	0	0	0	0	0	0	0	1	1	0	0	6	1	0	2	2	0	2	1	0	5	2	3	6	5	1	2	4	7	2	1	5	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	2	2	0	0	0	0	1	0	7	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	0	0	\N	\N	0	0	1	\N	\N	\N	\N	\N	\N	4	0	1	2018-11-23	0
276	357	4	0	2	3	0	\N	1	0	2	3	2	3	1	4	5	1	3	0	0	5	0	0	0	2	0	1	1	0	0	0	1	8	1	1	1	\N	0	0	0	7	2	\N	0	0	0	\N	2	2	3	1	1	1	{4}	6	1	\N	1	\N	2	4	4	0	1	0	2	2	3	3	4	0	1	4	3	1	0	5	2	0	3	2	0	3	1	0	5	0	2	3	6	0	5	3	1	2	2	4	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	4	7	6	0	4	1	0	1	\N	\N	\N	\N	0	0	0	0	0	0	7	0	0	0	0	0	2	0	1	\N	0	0	0	0	0	4	0	3	2018-11-23	7
277	356	4	0	2	3	0	\N	1	0	2	3	2	4	0	4	3	2	3	0	0	5	5	0	2	2	0	1	1	2	0	0	7	5	1	1	0	\N	0	1	0	3	0	6	0	0	2	1	1	0	2	1	1	0	{4}	4	1	\N	1	0	0	0	0	0	0	0	5	1	1	1	2	0	2	1	2	1	0	6	1	1	3	1	0	1	1	1	6	1	2	6	3	1	1	4	1	1	1	1	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	5	2	6	0	1	1	1	1	\N	\N	\N	\N	0	0	0	1	0	0	0	1	1	0	0	0	3	0	1	\N	\N	\N	\N	\N	0	2	0	3	2018-11-23	2
278	312	4	0	1	1	2	6	1	0	1	3	2	4	0	4	3	0	3	0	0	2	0	0	4	2	0	1	1	2	1	0	0	8	0	1	1	\N	1	1	0	2	2	5	0	0	0	\N	4	4	1	1	1	1	{3}	6	1	1	1	4	0	5	0	1	1	1	1	0	1	1	1	0	1	2	4	0	0	4	1	1	8	1	0	1	0	0	4	2	2	5	2	0	0	3	2	0	0	1	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	0	0	2	0	2	5	5	1	\N	\N	\N	\N	0	0	0	1	0	0	5	0	0	0	0	0	1	0	1	\N	0	\N	\N	2	0	3	1	1	2018-11-14	0
279	358	4	0	0	4	2	2	1	2	2	3	0	4	0	4	5	2	0	0	0	1	1	4	1	2	2	1	0	0	6	0	2	7	2	1	1	\N	3	1	1	5	0	12	0	1	0	\N	4	4	0	0	1	0	{3}	6	1	1	1	0	2	0	0	0	0	0	8	8	0	2	8	0	8	8	8	8	8	8	1	8	8	1	0	1	1	8	8	5	8	8	8	5	8	4	8	1	8	8	1	\N	5	\N	\N	\N	1	{}	\N	\N	6	6	2	5	7	5	1	3	9	0	1	\N	\N	\N	\N	\N	\N	0	4	0	0	5	0	0	8	3	0	4	0	1	\N	0	0	0	3	0	3	3	3	2018-11-23	5
280	311	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-14	\N
272	331	4	0	0	3	2	6	1	0	1	2	3	4	1	2	4	1	3	0	0	5	0	0	0	4	0	1	1	0	0	0	7	5	0	1	1	\N	2	1	0	1	2	\N	0	0	1	\N	3	1	1	1	1	1	{0,3,4}	6	1	\N	1	5	0	0	4	0	3	0	3	0	0	1	1	0	1	2	2	0	5	5	0	0	3	0	0	0	1	1	4	0	3	5	5	0	0	3	0	1	2	1	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	1	2	1	3	6	0	2	2	2	0	0	0	0	0	0	0	0	4	1	0	6	0	0	0	0	0	5	0	1	\N	\N	\N	\N	\N	0	3	0	3	2018-11-23	3
281	314	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	{}	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2018-11-23	\N
282	359	4	0	0	3	0	\N	1	1	1	3	3	4	1	4	4	1	3	0	0	5	5	1	0	2	0	1	1	0	0	0	0	8	2	1	1	\N	0	1	1	\N	1	\N	0	0	1	\N	0	2	0	1	1	1	{0}	7	1	\N	1	5	0	0	0	0	0	0	2	3	4	3	4	1	4	2	4	1	2	6	2	1	4	4	0	2	1	1	3	1	3	6	5	1	5	2	3	1	1	2	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	1	5	5	6	0	4	9	8	1	\N	\N	\N	\N	0	0	1	1	0	1	7	1	1	1	0	0	1	0	1	\N	0	0	0	0	0	3	1	2	2018-11-23	5
283	334	4	0	1	2	2	6	0	0	1	3	3	4	1	2	3	2	0	0	0	5	5	0	1	4	0	1	1	3	0	0	\N	5	1	0	1	\N	1	2	0	0	0	4	0	0	2	\N	2	1	2	1	1	1	{0,3,4}	6	1	1	1	2	0	0	4	0	2	0	3	3	0	1	2	0	1	1	3	0	0	6	1	0	2	3	1	1	1	1	6	1	2	6	2	0	3	1	1	1	0	4	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	5	0	\N	0	2	0	2	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	\N	\N	\N	\N	\N	1	0	1	\N	\N	\N	\N	\N	0	3	0	2	2018-11-23	0
284	361	4	0	0	0	2	6	0	1	2	3	4	2	0	4	3	0	3	0	0	3	5	4	3	1	0	1	1	0	0	2	1	5	2	1	1	\N	2	2	0	0	0	12	0	1	1	\N	1	1	2	1	1	0	{0}	1	0	1	1	4	2	4	0	0	3	2	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	4	4	4	0	3	1	0	1	\N	0	0	0	0	\N	1	4	0	1	\N	0	0	0	0	0	2	0	1	\N	0	0	0	0	0	\N	0	4	2018-10-02	4
285	362	4	1	1	1	0	\N	1	3	3	3	1	3	1	2	2	1	0	1	0	0	5	1	0	2	0	1	1	3	0	0	2	9	1	1	1	\N	2	2	0	0	0	6	0	0	0	1	3	2	0	1	1	1	{}	2	1	1	1	2	2	0	4	0	1	2	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	6	\N	\N	0	\N	1	0	1	0	5	0	7	0	0	0	0	\N	1	0	0	1	\N	0	0	0	0	0	0	0	1	\N	0	0	0	0	0	4	0	2	2018-10-17	2
286	360	4	0	2	0	\N	\N	1	1	1	3	3	3	1	2	5	1	1	0	0	5	5	0	2	1	0	1	1	0	0	0	0	4	\N	1	1	\N	1	2	0	5	0	6	0	0	1	\N	2	3	1	1	1	1	{0,7}	1	1	1	0	0	2	0	0	0	0	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	4	\N	\N	\N	\N	\N	1	2	5	7	0	6	0	0	0	0	\N	0	2	0	0	5	2	6	4	2	2	3	0	1	\N	0	0	0	1	1	2	1	1	2003-10-17	0
287	366	3	0	0	2	1	6	1	1	2	3	3	4	0	4	3	0	2	0	0	5	5	4	1	3	0	1	1	0	0	0	0	9	1	1	1	\N	1	1	0	0	0	2	0	0	1	\N	1	1	0	1	1	1	{}	6	0	0	0	0	2	0	0	0	0	0	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	\N	4	\N	6	0	2	4	2	0	5	2	1	1	2	1	0	1	1	0	2	2	5	1	4	2	2	0	0	5	2	2	0	1	0	4	2	4	2018-10-02	1
289	365	4	0	2	2	0	\N	1	1	0	3	4	4	0	4	5	1	1	0	0	5	5	2	0	2	0	1	0	0	1	0	1	5	2	1	1	\N	0	2	1	\N	2	\N	0	0	2	\N	0	2	0	1	1	1	{3}	6	1	1	1	3	2	4	4	0	3	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	7	1	2	2	7	6	1	4	3	5	1	\N	0	0	0	0	\N	0	0	3	1	\N	0	0	0	0	0	3	0	1	\N	0	0	0	3	0	0	0	0	2018-10-02	7
290	367	4	0	1	3	3	6	0	1	0	3	2	4	0	4	3	1	3	0	0	4	0	2	0	3	0	1	1	2	0	2	2	5	1	1	1	\N	1	1	0	1	2	12	0	1	2	\N	1	2	0	1	1	1	{4}	6	1	1	1	4	0	0	4	0	4	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	\N	1	7	\N	6	0	2	1	4	1	\N	0	0	0	0	\N	0	0	0	0	0	0	0	0	0	0	0	0	0	\N	0	\N	\N	\N	\N	\N	\N	3	2018-10-02	3
291	368	3	0	2	1	1	2	0	1	0	3	4	3	1	1	3	1	1	0	0	5	0	1	0	2	0	1	1	0	0	0	0	9	0	1	1	\N	0	0	1	0	2	6	0	0	0	\N	0	1	0	1	1	1	{0}	5	1	1	1	0	0	3	3	0	3	4	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	\N	7	\N	6	0	3	1	5	1	\N	0	0	0	0	0	0	0	0	0	3	0	0	0	0	0	0	0	1	\N	0	0	0	0	0	1	0	0	2018-10-02	2
292	371	1	0	0	2	1	\N	0	1	0	0	2	4	1	2	5	0	3	0	0	3	0	0	1	1	0	1	1	0	1	0	0	1	0	1	1	\N	1	0	0	0	0	6	0	1	1	\N	1	2	3	1	1	1	{0}	5	0	0	1	0	2	5	1	0	3	0	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	5	7	6	1	4	2	6	1	\N	0	0	0	0	\N	1	0	0	0	\N	0	1	0	0	0	1	0	1	0	0	0	0	1	0	0	0	4	2018-10-02	7
293	369	1	0	0	1	2	6	1	1	1	3	4	4	0	4	5	1	2	3	1	5	5	1	2	1	0	1	1	0	0	1	0	8	0	1	\N	\N	0	1	0	2	0	11	0	0	1	\N	4	2	1	0	1	0	{}	1	1	\N	0	0	2	0	5	\N	3	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	1	\N	\N	7	\N	6	0	1	3	6	1	\N	0	0	2	\N	\N	0	0	0	1	\N	\N	0	0	0	0	0	0	1	\N	0	0	0	0	0	1	4	0	2018-10-02	1
294	372	4	0	0	3	1	6	0	0	0	0	4	4	0	4	4	1	0	0	0	5	5	0	3	2	0	1	1	1	1	0	0	1	0	1	1	\N	2	0	1	0	0	6	0	0	3	\N	4	0	2	1	1	1	{0,2,6}	4	0	0	1	0	2	0	0	0	0	0	5	2	3	2	3	1	2	3	5	0	1	5	2	1	5	2	1	2	3	1	8	3	5	6	7	0	1	2	4	1	1	3	1	1	0	\N	1	\N	1	{}	\N	\N	0	0	0	5	7	1	1	4	4	3	1	\N	\N	\N	\N	\N	\N	0	1	0	0	0	1	1	5	1	0	3	0	1	0	\N	0	0	1	1	1	0	0	2018-11-23	0
295	374	4	0	1	3	1	\N	1	1	0	3	1	1	0	2	3	1	2	0	0	4	5	0	0	2	0	1	1	0	0	0	7	8	1	1	1	\N	0	0	1	6	2	\N	0	0	0	\N	1	2	0	1	1	1	{0,3,4}	7	1	\N	1	0	0	0	4	0	3	0	1	0	0	1	3	0	2	2	3	1	1	6	2	2	3	2	0	1	1	1	6	3	3	6	6	1	1	3	0	1	1	6	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	3	0	0	0	2	3	3	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	1	0	1	\N	0	0	0	0	0	4	1	3	2018-11-23	1
296	373	4	0	0	0	4	6	1	1	4	3	4	4	0	4	5	1	1	0	0	4	5	0	1	4	0	1	1	0	0	0	2	0	0	1	0	\N	2	2	0	0	0	4	0	0	1	1	1	2	0	1	1	1	{3}	7	1	\N	0	0	2	2	5	0	0	0	0	2	7	1	1	1	5	1	2	2	1	5	5	1	2	1	1	2	1	1	5	5	5	6	6	5	7	6	6	3	4	8	7	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	0	5	0	4	1	3	2	0	1	\N	0	0	0	0	0	1	0	0	0	7	1	2	4	0	0	3	0	1	\N	0	0	0	2	0	0	2	2	2018-11-19	1
297	375	4	0	0	4	0	6	1	1	2	3	3	4	1	2	2	2	1	0	0	5	0	0	0	1	0	1	1	0	1	0	0	9	0	1	1	\N	1	2	1	\N	0	6	0	0	0	\N	0	2	0	1	1	1	{4}	7	1	\N	1	4	2	0	0	0	4	0	5	0	0	5	0	0	1	3	0	0	0	5	1	0	6	1	0	1	0	5	1	1	0	0	5	1	0	5	2	1	0	2	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	0	0	0	3	0	1	4	4	1	\N	\N	\N	\N	\N	\N	0	0	0	0	3	0	0	8	0	0	1	0	1	\N	0	0	0	0	0	4	0	4	2018-11-23	0
298	376	4	0	0	3	1	3	1	1	3	3	3	3	0	2	4	1	3	1	0	5	5	0	0	3	0	1	1	0	0	0	0	8	1	1	1	\N	1	0	1	10	0	6	0	0	1	\N	3	3	0	1	1	1	{0,4}	6	1	\N	1	4	2	0	0	0	3	0	2	5	1	2	1	0	2	2	5	1	0	3	3	1	5	3	1	2	3	0	1	2	5	5	5	0	3	2	4	1	2	5	1	\N	\N	\N	\N	\N	1	{}	\N	\N	3	1	\N	1	1	3	0	1	5	8	1	\N	0	0	0	2	6	0	4	0	0	6	0	0	0	0	0	3	0	1	\N	0	0	0	0	\N	0	1	2	2018-11-23	1
299	379	4	1	2	2	1	6	\N	1	3	3	1	2	0	3	\N	0	2	0	0	0	5	0	1	1	0	1	1	2	2	0	0	\N	1	1	1	\N	2	2	0	5	0	4	0	0	2	\N	3	1	2	1	1	0	{0,4}	7	1	\N	1	4	2	0	0	0	4	0	5	0	1	3	0	0	1	5	5	1	0	6	1	3	4	4	1	3	3	1	6	3	3	3	3	0	3	5	3	2	1	6	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	0	1	2	6	0	3	3	2	1	\N	\N	\N	\N	0	\N	0	1	0	0	8	0	0	0	0	0	2	0	1	\N	0	\N	\N	0	0	4	2	0	2018-11-23	2
300	378	4	0	0	4	0	\N	1	1	0	3	1	4	0	4	4	1	3	0	0	5	0	0	0	2	0	1	1	0	3	0	0	\N	0	1	1	\N	1	1	0	0	0	12	0	1	1	\N	2	2	0	1	1	1	{0,2,6}	6	1	1	\N	4	2	0	4	1	4	1	3	3	3	2	2	0	8	5	2	6	0	5	1	2	4	4	0	5	1	1	5	0	0	5	3	1	6	3	0	1	1	1	1	0	\N	\N	\N	\N	0	{1,2}	\N	\N	0	1	1	5	0	6	0	2	1	8	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	\N	\N	\N	\N	\N	0	\N	\N	0	0	0	0	\N	4	1	4	2018-11-23	0
301	380	5	0	0	3	2	6	0	0	0	2	3	3	1	2	5	2	0	0	0	3	0	2	0	2	0	1	1	0	0	2	0	9	0	1	1	\N	1	\N	1	\N	1	12	0	0	1	\N	1	2	0	1	1	1	{2,6}	6	1	1	1	2	4	0	3	2	2	0	0	2	3	2	1	0	1	2	3	3	0	1	4	1	1	1	0	1	2	0	6	1	2	0	1	0	0	2	2	1	1	3	2	0	5	\N	0	1	1	{1}	0	6	0	0	2	5	4	6	0	4	6	5	1	\N	\N	\N	\N	0	0	1	0	0	0	3	1	2	3	2	0	2	0	1	\N	0	0	0	0	\N	0	2	0	2018-11-19	1
302	383	3	0	0	3	0	2	0	1	1	3	4	4	0	3	5	1	3	0	0	5	5	4	4	2	0	1	0	2	0	0	0	6	2	1	1	\N	1	1	0	0	0	4	0	0	1	\N	1	3	3	1	1	1	{0}	7	1	\N	1	0	2	0	5	0	3	0	6	1	0	0	1	0	1	0	3	0	0	7	1	0	6	0	0	0	1	4	2	1	4	6	3	0	3	4	4	1	2	4	0	0	\N	\N	\N	\N	1	{}	\N	\N	5	1	0	5	0	0	0	2	1	5	1	\N	\N	\N	\N	0	0	0	1	0	0	5	0	0	0	0	0	3	0	1	\N	\N	\N	\N	1	0	4	3	1	2018-11-23	2
303	382	4	0	0	3	1	6	0	0	1	3	1	3	0	3	3	1	3	0	0	4	5	1	3	1	0	1	1	0	0	0	2	9	0	1	0	\N	1	1	1	10	2	12	0	0	1	0	1	1	2	1	1	1	{1,3,4,5,7}	6	1	1	1	4	2	4	3	0	2	0	0	3	1	1	1	0	1	3	3	0	1	6	1	0	3	1	0	3	3	1	3	1	3	1	3	0	1	2	3	1	3	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	4	0	0	0	1	0	1	0	7	1	4	0	1	0	0	1	0	0	6	1	1	1	1	0	3	0	0	7	1	0	0	3	1	2	0	1	2018-11-23	0
304	385	4	0	3	3	0	4	1	0	1	3	1	4	0	3	3	1	0	0	0	5	5	1	0	2	0	1	1	0	0	0	0	\N	1	1	1	\N	1	1	1	\N	0	4	0	1	1	\N	1	1	0	1	1	1	{3,4,5}	5	1	\N	1	1	2	0	1	0	1	0	0	0	0	1	1	0	1	1	1	1	0	4	1	0	3	3	0	1	1	1	1	1	1	0	4	0	1	4	4	1	3	0	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	3	5	1	0	2	1	1	1	\N	0	0	0	0	0	0	0	0	0	7	0	0	\N	1	0	2	0	1	\N	0	0	0	2	0	3	1	0	2018-11-23	0
305	384	4	0	4	3	2	\N	1	0	2	3	4	4	1	4	3	1	0	0	0	5	0	2	0	3	0	1	0	0	0	0	7	5	1	1	1	\N	1	2	1	6	0	6	0	0	1	\N	1	2	0	1	1	1	{4}	1	1	\N	1	0	2	0	0	2	4	0	1	1	1	2	3	0	0	1	0	0	0	6	0	1	0	1	0	1	1	0	1	2	0	3	0	0	\N	3	0	2	1	3	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	0	0	5	0	2	0	2	1	6	1	\N	\N	\N	\N	\N	\N	0	1	0	1	\N	\N	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	1	0	3	1	0	2018-11-23	0
306	387	4	0	2	3	3	3	0	0	4	3	4	4	1	3	4	0	2	1	0	5	5	0	4	2	0	1	0	1	0	3	1	5	0	0	1	1	2	1	0	6	0	3	0	0	1	\N	4	3	1	0	1	1	{4}	4	1	\N	1	2	2	0	4	0	4	0	0	5	2	1	1	0	0	1	5	2	0	5	2	1	2	2	0	1	1	2	2	1	1	6	5	2	1	3	2	1	2	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	4	3	6	0	2	1	5	0	8	0	0	0	1	6	0	4	0	0	6	1	1	6	\N	1	3	0	0	8	0	0	0	2	0	3	0	0	2018-11-23	0
307	386	5	0	0	2	0	\N	1	1	1	2	3	4	1	4	3	2	3	0	0	4	0	0	0	2	0	1	1	1	1	0	0	7	2	1	1	\N	1	3	0	5	0	12	0	0	3	\N	1	2	0	1	1	1	{0,3,4}	2	1	\N	1	2	2	2	0	0	3	1	0	6	0	0	3	0	0	1	5	0	0	6	1	1	1	3	1	2	0	0	6	1	3	6	4	0	4	3	1	1	1	1	1	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	0	0	1	6	0	1	2	8	1	\N	\N	\N	\N	0	\N	0	0	0	0	3	0	0	0	0	0	5	0	1	\N	0	0	0	0	0	3	3	1	2018-11-23	1
308	388	4	0	0	0	0	6	1	0	3	3	4	4	1	3	4	1	0	3	5	2	1	4	4	2	7	1	1	7	7	5	3	0	0	0	1	3	2	2	0	1	0	10	0	0	2	\N	2	1	2	1	1	1	{4}	1	0	1	1	0	2	0	0	0	4	2	0	1	1	1	2	0	0	1	3	0	0	5	3	2	1	1	0	2	0	0	3	3	3	2	1	0	2	3	6	2	2	2	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	0	0	0	0	1	1	3	1	\N	\N	\N	\N	0	0	0	4	2	0	0	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	\N	2	0	1	2018-11-23	0
309	390	4	0	3	2	2	6	1	0	3	3	4	4	1	4	4	2	3	0	0	4	0	2	0	1	0	1	1	0	0	0	2	1	1	1	1	\N	0	1	0	0	2	6	0	0	1	\N	1	2	1	1	1	1	{4,6,7}	4	1	\N	1	4	2	0	2	0	3	0	2	3	2	3	3	0	1	2	3	0	0	5	1	1	0	1	0	0	1	1	5	1	5	5	6	2	2	5	2	1	2	5	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	0	0	3	1	6	0	2	2	2	1	\N	\N	\N	\N	0	0	0	1	0	0	3	0	0	0	0	0	2	0	1	\N	0	0	0	1	0	3	2	1	2018-11-19	2
310	389	5	1	4	2	1	6	1	0	3	2	4	4	1	4	4	1	0	0	0	5	0	0	0	1	1	1	1	3	0	0	7	9	0	1	1	\N	1	1	0	0	0	12	0	0	2	\N	4	2	0	1	0	1	{3,4,5}	4	1	\N	0	0	4	4	0	0	3	1	6	6	1	0	5	0	1	1	5	0	0	6	0	0	1	0	1	0	0	0	5	0	6	6	5	0	1	1	1	0	0	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	0	0	0	1	0	0	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	\N	\N	\N	\N	\N	5	0	1	\N	0	\N	\N	\N	0	2	3	0	2018-11-19	0
311	391	4	0	0	2	0	\N	1	0	4	3	3	3	1	2	5	1	2	0	0	4	0	2	3	4	0	1	1	0	0	0	0	4	1	1	1	\N	2	0	0	6	0	0	0	0	1	\N	1	2	1	1	1	1	{4}	6	1	\N	1	0	2	5	5	0	\N	0	1	1	0	2	3	0	1	3	1	1	3	4	0	1	3	1	0	1	1	1	3	3	5	5	5	2	4	3	2	1	2	3	3	0	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	3	5	6	0	4	0	5	1	\N	\N	\N	\N	0	\N	0	0	0	0	6	0	0	0	0	0	1	0	1	\N	0	0	0	5	0	3	0	2	2018-11-23	3
312	392	4	0	0	4	0	\N	1	0	0	3	2	4	1	4	5	1	2	0	0	5	0	0	0	3	0	1	1	0	0	0	0	\N	1	1	1	\N	1	1	0	1	0	0	0	0	2	\N	1	2	1	1	1	1	{4}	6	1	\N	1	0	2	0	5	0	4	0	0	3	0	0	1	0	1	1	3	0	1	2	0	0	1	0	1	0	1	0	0	4	4	4	3	0	3	3	0	0	0	0	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	0	0	5	5	6	0	4	1	2	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	0	0	0	0	1	0	1	\N	0	0	0	0	1	4	2	3	2018-11-19	5
313	395	5	0	0	3	2	6	1	0	0	3	1	4	1	4	4	1	3	0	0	3	0	4	0	3	0	1	1	0	0	0	0	8	1	1	0	\N	1	1	0	10	2	6	0	0	1	0	3	3	1	1	1	1	{6}	6	1	1	1	0	0	0	4	\N	3	0	5	5	1	3	3	0	1	1	5	3	0	6	1	2	5	1	0	3	2	1	6	1	5	5	3	2	1	3	3	2	2	5	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	0	0	4	1	1	0	1	2	8	1	\N	\N	\N	\N	0	0	0	1	0	0	6	0	0	0	0	0	5	0	1	\N	0	0	0	0	0	0	1	2	2018-11-23	0
314	393	4	0	0	2	0	\N	1	1	0	3	1	4	1	4	5	1	0	0	0	5	0	0	0	2	0	1	1	0	1	0	0	9	0	1	0	\N	2	1	0	1	2	6	0	0	0	0	0	2	0	1	1	1	{2,4,6}	6	1	\N	1	0	0	0	0	0	3	0	0	0	0	4	2	0	2	2	6	5	7	2	2	2	2	2	1	0	2	0	5	2	2	2	7	2	3	3	4	3	0	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	2	0	1	0	3	1	1	1	\N	\N	\N	\N	\N	0	1	0	0	0	5	0	0	0	0	0	1	0	1	\N	0	0	0	0	0	4	4	1	2018-11-19	2
315	396	5	0	0	1	2	6	1	0	1	2	3	3	0	4	4	2	3	0	0	4	4	1	1	2	0	1	1	1	3	0	2	1	2	1	1	\N	2	1	0	0	0	2	0	0	2	\N	1	2	0	1	1	1	{4}	4	1	\N	1	0	2	0	0	2	0	2	5	0	0	1	0	0	0	1	0	0	0	5	0	0	0	1	0	0	0	0	1	0	5	5	2	0	1	3	3	0	0	4	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	0	0	2	6	0	2	1	2	1	\N	\N	\N	\N	0	0	1	1	4	0	7	0	\N	\N	\N	\N	2	0	1	\N	0	\N	\N	2	0	3	0	0	2018-11-23	2
316	394	4	0	1	2	1	2	1	\N	1	2	4	4	1	4	4	1	3	0	0	4	5	4	0	2	0	1	1	0	0	0	7	1	0	1	1	\N	1	1	0	9	2	6	0	0	1	\N	1	2	1	0	1	1	{0}	6	1	\N	1	0	2	0	0	2	3	1	5	3	1	2	1	0	2	1	2	0	0	5	1	2	2	1	1	3	1	0	2	0	0	2	3	1	4	5	2	1	1	1	1	0	\N	\N	\N	\N	1	{}	\N	\N	3	0	0	0	5	3	0	4	2	1	1	\N	\N	\N	\N	0	0	0	0	0	0	3	0	0	0	0	0	2	0	1	\N	\N	\N	\N	\N	0	4	2	1	2018-11-23	5
317	398	4	0	4	0	1	2	1	0	2	2	4	4	1	4	4	1	0	3	5	3	1	4	4	1	7	1	1	7	7	5	3	8	0	1	1	\N	1	2	0	1	0	6	0	0	1	\N	4	0	0	1	1	1	{4}	4	0	1	1	0	2	3	0	0	4	3	0	1	3	4	0	0	1	1	5	1	1	5	1	0	1	1	0	0	0	0	5	5	5	5	5	0	1	3	0	1	0	2	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	0	0	0	0	0	1	1	1	7	1	\N	\N	\N	\N	0	0	0	0	0	0	7	0	0	0	0	0	1	0	1	\N	\N	\N	\N	\N	0	4	0	0	2018-11-23	0
318	397	5	0	1	1	2	6	1	0	0	2	4	4	0	3	2	1	3	0	0	4	5	0	1	2	0	1	1	0	1	0	0	7	2	1	1	\N	2	1	1	0	0	6	0	0	1	\N	2	1	0	1	1	1	{2}	7	1	1	1	3	2	3	3	0	3	1	4	4	2	1	3	0	1	1	2	0	0	6	2	1	2	3	0	2	2	1	3	1	3	2	2	1	0	2	6	1	2	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	6	2	6	0	2	2	1	1	\N	\N	\N	\N	0	0	0	1	1	1	\N	\N	\N	\N	\N	\N	\N	1	1	\N	\N	\N	\N	\N	0	4	1	0	2018-11-23	2
319	399	5	0	\N	0	0	3	1	0	0	3	4	4	0	4	5	\N	3	0	0	1	5	1	1	2	0	1	0	0	0	0	0	9	1	1	1	\N	1	0	1	10	2	12	0	0	1	\N	1	3	0	1	1	1	{2}	7	1	\N	1	0	1	0	0	0	4	0	2	2	2	2	2	0	2	0	3	5	0	5	0	0	2	2	0	0	2	0	0	6	7	5	0	0	5	3	3	1	0	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	0	4	5	1	0	4	3	2	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	0	2	2	4	2018-11-23	0
320	401	5	0	1	2	2	2	1	0	1	3	3	3	1	3	3	2	3	0	0	4	0	1	0	3	0	1	1	0	0	0	7	5	1	1	1	\N	1	0	0	2	0	11	0	1	1	\N	2	1	2	1	1	1	{0}	6	1	1	1	0	2	0	2	0	2	0	1	1	1	1	3	0	1	2	4	1	1	6	1	0	3	1	0	1	1	0	2	0	3	4	2	0	2	4	2	1	1	3	2	0	\N	\N	\N	\N	0	{}	\N	\N	3	1	2	5	4	2	0	3	3	4	1	\N	\N	\N	\N	1	0	0	1	0	1	\N	0	\N	\N	0	\N	2	0	1	\N	0	0	0	0	0	3	0	1	2018-11-19	2
321	402	3	0	1	3	0	\N	1	1	3	3	3	3	0	2	5	1	0	0	0	5	5	0	0	3	0	1	1	0	0	0	0	\N	1	0	1	\N	1	0	1	\N	2	\N	0	0	0	\N	2	2	0	1	1	1	{0,3}	7	1	\N	1	4	2	0	4	0	3	0	6	6	2	2	2	0	2	2	3	0	0	6	1	0	5	3	1	1	2	1	2	2	3	6	4	0	6	2	1	1	1	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	4	0	0	0	2	2	2	1	\N	\N	\N	\N	0	0	1	0	0	0	6	0	0	0	0	0	1	0	1	\N	0	0	0	0	0	4	1	1	2018-11-23	0
322	400	5	0	1	2	2	2	1	0	1	3	3	3	1	3	3	2	3	0	0	4	0	1	0	3	0	1	1	0	0	0	7	5	1	1	1	\N	1	0	0	2	0	11	0	1	1	\N	2	1	2	1	1	1	{0}	6	1	1	1	0	2	0	2	0	2	0	1	1	1	1	3	0	1	2	4	1	1	6	1	0	3	1	0	1	1	0	2	0	3	4	2	0	2	4	2	1	1	3	2	0	\N	\N	\N	\N	0	{}	\N	\N	3	1	2	5	4	2	0	3	3	4	1	\N	\N	\N	\N	1	0	0	1	0	1	\N	0	\N	\N	0	\N	2	0	1	\N	0	0	0	0	0	3	0	1	2018-11-23	2
323	405	4	0	1	0	0	\N	1	1	3	1	3	4	1	3	3	1	1	0	0	3	0	0	0	1	0	1	1	0	0	0	0	\N	0	1	1	\N	1	1	0	5	0	\N	0	1	1	\N	1	2	1	1	1	1	{2,4,6}	4	1	\N	1	0	0	0	2	0	4	0	5	5	1	2	1	0	3	1	3	1	3	6	1	1	6	3	0	1	1	1	7	3	6	6	6	1	3	5	1	1	1	1	1	0	5	9	0	12	1	{1,2,3}	0	8	0	\N	0	0	0	0	0	1	2	1	1	\N	\N	\N	\N	0	0	1	0	0	1	\N	0	0	0	0	0	0	0	1	\N	\N	\N	\N	0	0	4	4	1	2018-11-18	\N
324	408	4	0	0	4	0	\N	1	1	0	3	3	4	0	4	4	1	3	0	0	5	0	0	1	2	0	1	1	0	0	0	0	5	1	1	1	\N	1	1	0	3	2	\N	0	0	2	\N	1	3	1	1	1	1	{4}	6	1	\N	1	4	0	0	4	0	4	0	0	0	1	2	3	0	2	3	1	2	0	6	5	0	0	2	0	2	2	0	6	1	2	5	0	0	1	3	6	1	1	2	1	0	5	9	1	\N	0	{3}	0	11	0	\N	0	2	2	6	0	3	0	2	1	\N	\N	\N	\N	0	0	0	0	0	0	6	0	0	0	0	0	1	0	1	\N	\N	\N	\N	0	0	4	2	4	2018-11-23	2
325	407	3	0	2	1	2	6	1	0	2	3	3	2	0	3	5	0	1	0	0	5	5	2	2	2	0	1	1	0	1	0	1	0	1	1	1	\N	1	0	1	9	0	2	0	\N	2	\N	1	1	0	1	1	1	{1,2,3,6,7}	7	0	0	1	0	2	4	5	0	3	0	4	3	3	2	3	0	2	3	2	1	0	4	2	1	2	3	1	3	2	0	4	0	2	3	1	0	1	3	4	1	3	3	0	0	5	2	0	13	1	{}	0	10	0	\N	0	6	2	2	0	2	8	8	0	5	1	1	2	4	2	0	0	0	0	2	2	6	1	3	1	3	0	1	\N	\N	\N	\N	3	0	3	1	0	2018-11-19	1
326	406	4	0	0	0	1	6	0	0	3	3	4	4	0	4	4	1	2	0	0	5	5	4	0	3	0	1	1	0	2	0	1	8	2	1	1	\N	0	0	0	9	0	2	0	0	0	\N	0	2	2	1	1	1	{0,2,4,6}	4	1	1	1	0	2	0	0	0	3	0	5	0	0	1	0	0	4	0	4	5	0	4	3	0	1	0	0	4	0	0	8	4	8	6	1	4	8	5	1	3	6	2	0	0	5	8	1	\N	1	{2,3}	0	12	1	0	0	7	7	6	0	4	0	3	0	7	0	0	0	2	0	0	0	0	0	7	0	0	0	1	0	3	0	1	\N	\N	\N	\N	1	0	2	4	1	2018-11-19	2
327	410	4	0	0	2	3	6	0	0	3	3	2	4	0	3	3	0	2	0	0	2	5	0	1	2	\N	1	1	3	2	2	2	2	2	1	1	\N	1	2	0	0	0	12	0	0	1	\N	3	1	2	0	1	1	{3}	7	1	\N	0	0	2	0	0	0	2	2	3	4	2	2	0	0	0	2	6	2	0	6	1	1	3	2	0	0	2	1	6	0	1	5	6	1	1	7	2	0	1	3	3	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	0	0	0	\N	0	1	0	7	1	\N	\N	\N	\N	2	6	1	1	0	0	2	0	0	0	\N	0	2	0	1	\N	\N	\N	\N	\N	1	2	1	2	2018-11-23	0
328	409	4	0	0	3	0	\N	1	1	2	3	3	3	1	3	4	1	1	0	0	5	0	0	0	2	0	1	1	0	0	0	0	\N	1	1	1	\N	0	1	0	5	0	6	0	0	1	\N	2	3	1	1	1	1	{0,4}	6	1	\N	1	0	2	0	0	0	3	0	5	0	1	1	1	0	0	1	5	1	0	5	1	0	5	3	0	0	1	0	6	0	1	2	3	0	1	3	0	0	1	1	0	1	\N	\N	0	13	0	{2,3}	0	6	0	\N	3	4	0	\N	0	1	1	4	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	\N	\N	\N	\N	1	0	1	\N	\N	\N	\N	\N	0	4	1	3	2018-11-19	0
329	411	3	1	2	2	4	2	0	0	0	2	4	4	0	4	5	1	3	0	0	5	5	4	4	2	0	1	1	0	1	0	0	0	2	1	1	\N	1	1	1	0	0	6	0	1	2	\N	1	1	2	1	1	1	{0,2,6,7}	7	0	0	1	0	2	0	4	0	4	0	4	4	1	4	1	0	4	5	5	5	2	6	3	2	2	6	0	3	0	1	4	2	1	3	4	1	4	5	4	1	3	3	3	\N	\N	\N	\N	\N	0	{}	\N	\N	6	0	0	0	4	0	0	4	8	8	0	5	0	0	0	0	0	0	4	0	0	5	0	0	0	0	0	4	0	1	\N	\N	\N	\N	5	0	4	0	4	2018-11-19	5
330	412	4	0	0	4	0	1	1	1	1	2	4	4	1	3	4	1	3	0	0	5	0	0	0	3	0	1	1	0	0	0	0	\N	\N	1	1	\N	0	2	0	2	2	6	0	1	1	\N	1	1	0	1	1	1	{4}	5	1	1	1	2	0	0	1	0	2	0	4	4	0	2	1	0	2	2	2	2	0	6	5	0	1	2	1	2	1	1	1	1	6	1	1	5	1	6	5	0	3	3	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	1	2	2	1	0	2	1	6	1	\N	\N	\N	0	0	0	0	0	0	0	5	0	0	0	0	0	1	0	1	\N	\N	\N	\N	0	0	4	0	2	2018-11-19	3
331	413	3	0	0	3	0	6	1	0	1	3	3	4	0	\N	3	1	3	0	0	4	4	4	2	4	0	1	1	0	0	0	0	\N	2	1	0	\N	0	2	1	1	2	\N	0	0	1	0	1	3	1	1	1	1	{4,6,7}	4	1	1	1	0	2	0	4	0	3	0	6	6	3	3	4	0	0	4	6	3	0	5	1	0	1	3	0	3	1	1	0	0	0	5	0	0	1	5	3	1	3	1	3	1	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	1	3	6	0	1	1	2	1	\N	\N	\N	\N	0	0	1	2	0	1	\N	0	\N	\N	\N	\N	1	0	1	\N	\N	\N	\N	\N	0	3	0	3	2018-11-23	2
332	415	4	1	0	2	1	6	1	0	1	3	1	4	1	4	4	1	1	0	1	5	0	0	0	3	0	1	1	2	0	0	0	\N	1	1	1	\N	2	1	0	9	2	\N	0	1	1	\N	1	2	1	1	1	1	{4}	7	1	\N	1	0	2	5	0	0	3	1	5	1	0	3	2	0	1	3	3	1	1	6	1	0	3	1	1	2	1	1	6	1	3	5	4	0	3	2	1	1	1	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	0	0	2	6	0	3	0	\N	1	\N	\N	\N	\N	0	0	1	2	0	1	\N	\N	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	5	0	4	0	0	2018-11-19	2
333	414	4	1	2	3	2	6	0	0	2	3	2	4	1	4	4	0	2	0	0	5	5	1	0	1	0	1	1	0	1	1	0	\N	2	1	1	\N	1	1	1	\N	2	12	0	1	1	\N	1	2	3	1	1	1	{0,2,6}	7	1	\N	1	0	4	5	0	0	4	0	1	1	1	1	3	1	2	4	3	3	0	4	1	3	1	4	0	3	1	5	4	2	1	4	3	0	2	4	4	2	3	8	1	\N	\N	\N	\N	\N	1	{}	\N	\N	3	1	0	0	1	0	0	1	1	5	0	2	1	1	0	2	6	1	1	3	0	3	1	4	3	2	0	2	0	0	6	0	0	0	1	1	4	0	0	2018-11-19	1
334	417	4	0	0	4	0	\N	1	1	1	2	4	4	1	3	4	1	2	0	0	5	5	1	0	2	0	1	1	0	0	0	0	\N	0	1	1	\N	0	2	0	2	0	4	0	1	1	\N	1	1	0	1	1	1	{4}	3	1	1	1	2	0	0	3	0	2	0	4	4	0	2	2	0	2	2	2	2	0	5	3	0	2	2	0	1	1	1	6	1	1	5	1	0	2	3	3	1	1	3	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	1	1	2	1	0	2	1	4	1	\N	\N	\N	0	0	0	0	0	0	0	5	0	0	0	0	0	1	0	1	\N	\N	\N	\N	0	0	4	0	2	2018-11-19	3
335	418	4	0	1	1	0	3	1	0	2	3	2	4	0	3	2	0	0	0	0	2	5	4	0	2	0	1	1	1	2	1	2	5	2	1	1	\N	1	0	0	9	1	0	0	1	1	\N	3	3	1	1	1	1	{1,2,6}	7	1	\N	1	1	1	0	0	0	4	0	3	3	1	0	3	0	1	2	3	3	1	5	1	1	1	1	0	1	1	1	5	1	0	0	3	1	2	3	4	1	1	3	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	0	0	1	0	0	1	1	8	1	\N	\N	\N	\N	0	0	0	4	0	0	5	0	0	0	0	0	2	0	1	\N	\N	\N	\N	1	0	3	1	0	2018-11-19	0
336	416	4	0	2	1	2	6	0	0	1	3	4	4	0	4	3	1	1	0	0	5	5	0	0	1	1	1	1	2	1	1	0	9	0	1	0	\N	1	3	0	6	0	6	0	0	1	1	1	2	0	1	1	1	{0,4,6}	7	1	\N	1	0	2	0	0	0	3	0	2	5	5	2	0	0	5	1	0	6	2	6	2	1	6	3	0	1	6	0	7	0	0	6	2	1	2	4	3	0	4	2	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	0	0	0	\N	0	2	7	4	1	\N	\N	\N	\N	0	0	0	2	1	0	1	1	2	4	0	0	2	0	1	\N	\N	\N	\N	1	0	1	0	0	2018-11-23	0
337	419	4	1	0	3	0	\N	0	0	1	3	4	4	0	4	5	1	2	0	0	5	5	0	0	2	1	1	1	2	0	0	0	9	1	0	1	4	2	1	0	5	0	4	0	0	2	\N	2	1	2	1	1	1	{0,2,4,6}	7	1	\N	1	1	0	4	4	0	3	0	6	6	0	1	1	0	0	2	6	1	1	5	1	3	1	2	0	1	2	2	8	1	6	6	7	0	2	4	3	1	2	3	1	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	0	0	2	2	1	3	1	4	1	\N	\N	\N	\N	0	0	0	1	0	1	\N	0	0	0	\N	\N	5	1	1	\N	\N	\N	\N	5	0	4	2	1	2018-11-23	0
338	420	4	0	1	2	0	\N	1	0	2	3	2	4	1	3	4	1	1	0	0	5	0	0	0	1	0	1	1	3	0	0	0	\N	0	1	1	\N	1	1	0	1	0	11	0	0	1	\N	1	1	0	1	1	1	{0,4,6}	7	1	1	1	0	0	2	0	0	2	1	5	0	0	3	2	0	1	1	6	1	0	5	0	0	3	1	0	1	0	1	6	2	3	5	5	0	5	3	1	1	1	1	6	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	3	2	0	1	7	7	1	\N	\N	\N	\N	0	0	0	3	0	1	\N	0	0	\N	0	0	1	0	1	\N	\N	\N	\N	0	0	3	1	2	2018-11-19	0
339	421	4	0	2	2	1	\N	1	0	2	3	3	4	0	3	5	2	1	0	0	5	0	0	0	2	1	1	1	0	0	0	0	\N	2	1	1	\N	1	1	0	2	0	6	0	0	1	\N	1	2	1	1	1	1	{2,4,6}	6	1	1	1	1	0	2	0	0	3	2	4	3	4	6	2	0	3	3	3	1	0	3	2	2	3	2	0	3	2	0	3	0	1	1	3	0	2	3	2	1	1	4	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	2	1	0	1	7	6	1	\N	\N	\N	\N	0	0	0	0	0	0	5	\N	1	0	0	0	1	0	1	\N	\N	\N	\N	1	0	3	1	2	2018-11-23	0
340	422	3	1	2	2	2	3	1	0	0	2	4	4	1	3	4	2	1	0	0	5	0	0	0	3	0	1	1	1	0	0	0	\N	2	1	1	\N	2	2	0	0	0	11	0	0	1	\N	3	4	1	1	1	1	{0,3,4,5}	6	1	\N	1	0	2	0	4	1	0	1	3	0	0	0	0	0	0	1	0	0	0	4	0	0	1	0	1	0	0	1	4	5	3	5	4	1	1	1	1	0	0	1	0	\N	\N	\N	\N	\N	1	{}	\N	\N	1	4	0	0	1	6	1	1	0	0	1	\N	\N	\N	\N	0	0	0	0	0	\N	0	0	\N	0	0	0	0	0	1	\N	\N	\N	\N	0	0	4	0	0	2018-11-19	0
341	423	4	0	1	3	0	\N	1	1	3	1	3	4	1	4	5	1	3	0	0	3	0	0	0	2	0	1	0	0	0	0	0	1	1	1	0	\N	1	0	0	6	0	6	0	0	1	1	0	2	0	1	1	1	{2,4,6}	4	1	1	1	0	0	0	4	0	4	0	5	5	2	3	2	0	1	0	4	0	2	7	5	0	3	6	0	0	0	0	5	0	5	5	5	0	5	4	1	0	1	0	2	0	5	9	0	13	1	{1,2}	\N	\N	0	\N	0	0	2	1	0	1	1	1	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	0	\N	0	0	1	\N	\N	\N	\N	0	0	4	4	1	2018-11-19	0
342	424	4	0	2	2	1	6	1	0	3	3	4	4	0	4	4	1	2	0	0	5	5	0	2	2	0	1	1	0	0	0	0	8	0	1	1	\N	0	2	0	1	0	5	0	0	0	\N	3	1	0	1	1	1	{4}	4	1	\N	1	4	2	0	0	0	4	0	0	0	0	0	0	0	0	2	5	0	0	5	0	3	0	1	0	1	3	0	5	3	5	3	0	2	2	2	3	3	3	5	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	4	0	0	0	4	0	2	0	7	0	8	1	6	0	2	6	0	2	0	0	0	2	6	4	0	0	4	0	1	\N	\N	\N	\N	4	0	2	0	4	2018-11-19	0
343	426	4	0	2	1	2	3	1	0	2	3	2	4	1	4	3	1	0	0	0	4	0	4	0	2	0	1	1	0	0	0	0	\N	0	1	1	\N	1	2	0	5	2	\N	0	0	1	\N	1	2	1	1	1	1	{6}	6	1	\N	1	4	2	0	4	0	3	0	6	6	0	3	3	0	1	0	6	0	1	6	1	3	0	0	0	1	1	0	1	1	2	1	1	0	1	2	0	1	1	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	4	6	0	3	2	6	0	7	0	0	0	3	6	0	0	2	0	7	2	3	5	0	0	3	0	1	\N	\N	\N	\N	2	0	4	0	3	2018-11-19	3
344	427	4	0	2	2	3	0	0	0	2	1	3	4	1	4	4	1	2	0	0	5	0	2	0	2	0	1	0	0	2	0	0	\N	1	1	1	\N	2	1	0	3	0	0	0	0	1	\N	1	2	1	1	1	1	{0,2,3,4,5,7}	4	1	1	1	4	2	5	0	0	3	1	1	1	1	4	2	0	0	3	5	3	3	5	0	2	5	6	1	4	3	1	5	5	5	5	5	0	5	2	3	3	2	6	0	0	5	1	1	\N	1	{2}	0	6	6	0	0	0	1	6	0	3	3	1	1	\N	\N	\N	\N	0	0	0	0	0	0	6	1	5	4	1	0	2	0	1	\N	\N	\N	\N	3	0	4	4	0	2018-11-19	6
345	428	4	0	1	2	1	6	1	0	3	3	1	3	0	4	4	1	3	0	0	5	5	0	4	2	0	1	0	0	0	0	0	\N	1	1	1	1	2	1	0	5	0	4	0	0	1	\N	3	1	2	1	1	1	{0,4}	5	1	\N	1	5	0	0	0	0	3	0	0	0	0	0	0	0	0	2	1	0	0	4	7	6	1	1	0	2	6	0	7	1	6	7	0	0	0	3	3	0	0	0	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	0	1	2	6	0	3	3	6	1	\N	\N	\N	\N	0	0	0	0	0	0	7	1	2	4	0	0	2	0	1	\N	\N	\N	\N	1	0	4	0	0	2018-11-19	2
346	431	4	0	0	3	1	2	1	0	1	3	2	4	1	4	4	1	1	0	0	5	0	0	0	2	0	1	1	0	0	0	2	6	1	1	1	\N	2	0	0	0	0	11	0	0	1	\N	1	1	0	1	1	1	{3,4}	6	1	1	1	4	0	4	0	0	3	0	6	6	0	0	0	0	0	0	5	0	0	5	0	0	2	0	0	0	0	0	3	3	3	5	5	0	5	5	0	0	0	3	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	0	\N	0	3	1	3	1	\N	0	0	\N	0	0	0	2	0	1	\N	\N	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	2	0	4	0	1	2018-11-19	0
347	430	4	0	1	2	2	6	1	0	3	3	3	4	0	3	4	1	3	0	1	5	5	0	1	2	0	1	1	1	0	0	7	7	2	1	1	\N	1	1	0	2	0	4	0	0	1	\N	0	2	3	1	1	1	{4,6}	6	1	\N	1	0	0	0	0	0	3	2	2	2	5	0	2	0	1	2	0	0	0	5	0	2	3	3	0	1	2	0	7	0	8	7	8	0	8	3	1	0	0	5	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	4	4	0	3	0	0	1	\N	\N	\N	\N	0	0	0	1	0	0	3	0	0	0	1	0	2	0	1	\N	\N	\N	\N	1	0	3	2	2	2018-11-19	4
348	432	1	0	4	4	0	\N	1	0	0	3	4	4	1	2	5	1	0	0	0	5	0	0	0	3	0	1	1	0	0	0	0	\N	1	1	1	\N	0	0	1	\N	2	\N	0	1	1	\N	1	1	2	1	1	1	{3}	7	1	\N	1	0	\N	0	5	0	0	0	5	5	0	2	5	0	2	0	5	0	0	0	0	0	5	5	0	0	0	0	1	5	1	1	6	0	0	3	6	0	0	5	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	2	1	0	1	3	1	1	\N	\N	\N	\N	0	0	1	0	0	1	\N	0	0	0	\N	0	2	0	1	\N	\N	\N	\N	5	0	4	4	4	2018-11-19	0
349	435	4	0	0	2	1	2	1	0	0	3	2	4	0	4	4	1	0	0	0	5	5	2	2	2	0	1	1	1	0	0	2	9	2	1	1	\N	2	3	0	0	0	2	1	1	1	\N	2	2	0	1	1	1	{0,2,4,5,6,7}	1	1	\N	1	4	4	0	4	0	3	0	2	0	0	0	3	0	0	3	3	0	3	4	1	3	2	3	0	1	3	1	6	1	3	6	3	0	1	4	3	1	1	3	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	1	1	4	7	6	0	3	3	4	1	\N	\N	\N	\N	0	0	0	0	0	0	6	0	0	0	0	0	2	0	1	\N	\N	\N	\N	5	0	4	0	0	2018-11-19	7
350	434	4	1	0	2	3	3	1	0	1	3	4	4	0	4	5	0	1	0	0	5	5	0	1	2	1	1	1	0	0	0	2	9	1	1	1	\N	1	2	0	6	0	6	0	\N	0	\N	3	4	1	1	1	1	{2,5,6}	6	1	\N	1	0	2	0	0	0	1	0	1	1	2	1	1	1	2	1	5	2	0	8	1	1	5	5	1	2	1	0	5	5	5	6	3	0	5	6	2	2	2	1	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	0	\N	0	2	2	1	1	\N	\N	\N	\N	0	\N	1	3	0	1	\N	\N	\N	\N	\N	\N	1	0	1	\N	\N	\N	\N	1	0	3	2	2	2018-11-19	1
351	433	3	0	0	4	1	6	1	0	0	3	4	4	0	3	4	1	3	1	0	2	5	2	1	2	0	1	1	0	2	0	0	5	0	1	1	\N	1	1	0	5	1	12	0	0	0	\N	4	2	0	1	1	1	{2,3,4}	6	1	\N	1	4	0	0	0	0	3	1	2	5	0	1	0	0	5	0	5	0	0	5	0	0	5	0	0	0	0	0	5	2	2	2	0	0	2	3	2	2	0	2	0	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	6	0	7	5	6	0	4	4	5	1	\N	\N	\N	\N	0	0	0	4	1	\N	\N	\N	\N	\N	\N	\N	1	0	1	\N	\N	\N	\N	\N	0	4	0	1	2018-11-19	5
352	436	4	0	0	2	2	6	1	0	3	2	4	4	1	4	4	1	3	0	5	5	0	1	0	1	0	1	1	0	1	0	0	5	0	1	0	\N	1	3	0	1	0	5	0	0	0	1	3	3	1	1	1	1	{2,6,7}	6	1	\N	1	5	0	0	4	0	3	0	0	0	0	0	1	0	1	2	3	3	0	5	3	0	0	2	0	3	6	1	6	1	1	1	5	0	3	4	3	1	3	6	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	0	0	2	1	0	1	4	4	1	\N	\N	\N	\N	3	2	1	1	0	0	7	4	5	1	2	0	3	0	0	7	1	0	0	2	0	3	0	0	2018-11-23	0
353	437	4	0	0	3	0	\N	1	1	0	3	1	4	1	4	5	1	3	0	0	5	0	0	0	2	0	1	1	0	0	0	0	\N	0	1	1	\N	1	0	1	\N	0	12	0	1	0	\N	1	2	0	1	1	1	{0,4}	3	0	0	1	2	0	0	4	0	3	0	3	4	4	1	2	0	1	1	2	4	0	5	1	1	0	2	0	2	0	1	3	0	1	0	5	0	1	3	2	1	1	2	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	0	0	0	0	\N	0	2	0	0	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	0	0	0	0	1	0	1	\N	0	0	0	0	0	4	1	3	2018-11-19	0
354	439	4	0	1	1	2	2	1	1	3	2	2	3	1	2	4	1	3	0	0	4	0	0	2	2	0	1	1	0	0	0	0	\N	1	1	0	\N	2	2	0	5	2	12	1	0	1	1	3	2	1	1	1	1	{0,3,4,6}	6	1	\N	1	1	0	3	2	0	3	1	0	0	0	2	3	0	1	2	3	0	0	6	1	1	1	3	1	2	2	0	8	1	0	2	3	0	6	3	2	1	2	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	0	1	0	1	3	8	1	\N	\N	\N	\N	2	6	0	2	0	0	3	3	6	4	0	1	3	0	1	\N	\N	\N	\N	3	0	2	0	1	2018-11-19	0
355	440	4	0	1	3	0	\N	1	1	1	2	4	4	1	4	4	1	3	0	0	5	0	0	0	2	0	1	1	0	0	0	0	5	1	1	0	\N	0	0	0	1	2	\N	0	0	1	0	0	1	3	1	1	1	{0,4}	6	1	1	1	0	2	0	0	0	3	0	1	1	1	1	2	0	2	2	2	1	5	5	0	0	0	0	0	1	1	1	3	3	4	5	5	1	5	3	0	1	0	1	2	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	0	0	2	6	0	3	4	4	1	\N	\N	\N	\N	0	0	0	0	0	0	6	0	0	0	0	0	1	0	1	\N	\N	\N	\N	\N	\N	4	4	4	2018-11-19	2
356	443	4	0	2	1	1	6	0	0	2	3	3	4	1	3	4	2	1	3	0	5	0	2	2	2	1	1	1	0	0	0	2	9	0	0	1	5	2	0	1	\N	2	\N	0	0	2	\N	3	3	1	0	0	0	{1,7}	7	1	\N	1	4	2	1	0	0	4	1	6	6	6	5	0	0	0	0	5	0	2	6	2	0	0	0	0	0	0	0	6	2	6	0	7	0	2	4	1	1	1	2	1	\N	\N	\N	\N	\N	0	{}	\N	\N	5	1	0	0	1	6	0	1	0	8	1	7	\N	\N	\N	\N	6	1	2	0	0	5	4	6	4	2	1	3	0	1	\N	\N	\N	\N	3	1	2	0	0	2018-11-19	1
357	441	4	0	3	1	2	1	1	0	3	1	3	4	1	4	5	0	2	0	2	2	2	1	2	2	2	1	0	7	2	0	2	1	0	0	1	0	0	2	0	3	0	0	0	1	0	\N	4	1	0	0	0	1	{0,4,5}	7	0	1	1	5	2	4	4	0	1	1	5	5	0	0	1	0	0	0	3	1	0	0	4	0	0	5	0	1	4	0	7	1	0	5	3	0	2	4	3	0	3	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	1	1	0	1	2	2	0	1	1	6	0	7	4	2	2	5	2	0	4	4	0	2	4	6	1	1	2	3	1	0	6	4	4	0	3	1	3	0	0	2018-11-19	0
358	442	5	1	0	1	0	\N	1	1	0	3	4	4	1	3	4	1	2	0	0	3	0	1	4	2	1	1	1	3	3	0	7	8	1	1	1	\N	2	2	0	5	0	4	0	0	0	\N	1	2	1	1	1	1	{0,2,5,6}	4	1	\N	1	0	2	0	0	0	1	1	3	4	2	0	1	1	1	2	3	3	2	6	2	2	2	0	0	3	2	1	5	2	1	5	5	0	3	4	3	1	2	4	1	0	\N	\N	\N	\N	1	{}	\N	\N	0	1	0	0	2	6	0	3	3	6	0	8	0	0	0	1	0	0	1	0	0	7	3	4	7	1	0	4	0	1	\N	\N	\N	\N	1	0	4	1	1	2018-11-19	2
359	444	4	0	0	1	1	6	0	0	0	2	2	4	0	4	4	1	3	0	0	5	5	0	0	3	0	1	1	0	0	0	0	\N	0	1	1	\N	1	0	1	2	2	\N	0	0	1	\N	1	2	0	1	1	1	{0,6}	7	1	\N	1	4	2	0	0	0	3	0	0	2	0	3	0	0	2	3	3	1	0	4	2	1	2	2	0	2	0	3	2	3	4	4	0	0	1	4	1	1	1	4	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	4	6	0	4	1	1	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	1	0	4	0	2	2018-11-19	4
360	445	4	0	0	4	0	\N	\N	0	3	2	2	2	1	4	4	1	0	0	0	3	0	0	0	1	0	1	1	0	0	0	0	\N	1	1	1	\N	1	1	0	9	0	2	0	0	3	\N	4	2	3	1	1	1	{4}	7	0	0	1	0	2	5	0	0	0	0	3	3	3	1	5	0	1	5	1	0	0	1	1	1	1	3	0	1	3	0	3	1	0	0	2	0	3	4	4	1	1	4	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	3	0	\N	0	4	4	5	1	\N	\N	\N	\N	1	\N	0	1	0	1	\N	0	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	\N	2	1	0	0	2018-11-08	0
361	446	4	0	2	4	0	\N	1	1	2	3	3	4	1	4	2	1	0	0	1	\N	4	3	2	2	\N	1	1	\N	0	\N	\N	\N	0	1	1	\N	0	0	1	\N	1	\N	0	1	3	\N	1	1	2	1	1	1	{3}	3	1	1	\N	0	0	0	0	0	0	1	2	2	2	3	1	1	1	2	2	1	1	5	3	3	2	3	0	2	2	3	2	2	2	6	2	1	2	3	2	1	2	2	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	6	2	2	1	0	0	2	1	2	1	\N	\N	\N	\N	\N	0	1	1	0	0	2	\N	\N	\N	0	0	2	0	1	\N	\N	\N	\N	0	1	2	2	0	2018-11-08	1
362	447	4	0	4	1	2	2	0	0	0	2	1	4	0	4	3	2	0	0	0	1	5	4	3	4	0	1	1	0	0	1	\N	8	0	1	1	\N	0	0	0	6	1	0	1	1	2	\N	1	2	0	1	1	1	{0}	7	1	1	1	5	2	0	0	0	0	0	2	1	0	1	1	0	1	8	1	1	1	8	1	1	2	2	0	2	2	1	8	1	4	8	5	0	5	5	2	2	1	1	2	\N	\N	\N	\N	\N	0	{}	\N	\N	1	0	2	5	0	0	0	0	9	8	0	7	1	1	0	2	0	0	1	4	0	7	2	2	1	1	0	2	0	1	\N	0	0	0	2	1	0	1	0	2018-11-08	1
363	448	3	1	0	1	0	\N	1	0	0	3	4	4	0	4	5	1	0	0	0	5	0	1	0	2	\N	1	1	0	0	0	0	7	0	1	1	\N	0	0	1	\N	2	\N	0	0	0	1	0	2	0	1	1	1	{3}	7	1	1	1	0	2	0	5	0	0	2	0	0	1	0	0	0	0	0	5	8	1	8	7	3	4	0	0	1	0	0	0	0	8	8	1	8	8	6	0	0	0	0	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	0	0	1	6	0	1	1	0	1	\N	\N	\N	\N	\N	0	0	\N	0	1	\N	\N	\N	\N	\N	\N	0	0	1	\N	\N	\N	\N	0	1	2	3	2	2018-11-08	2
364	450	4	0	4	3	4	6	1	0	3	0	3	4	1	4	\N	2	3	0	1	5	0	0	0	1	0	1	1	0	0	0	7	\N	0	1	1	\N	0	1	0	0	0	12	0	0	0	\N	0	2	0	1	1	1	{0}	1	0	0	\N	0	0	0	5	0	0	0	7	7	0	0	7	0	8	0	6	0	0	7	2	1	0	0	0	0	0	0	0	1	1	0	8	8	5	3	5	3	0	0	0	0	\N	\N	\N	\N	1	{}	\N	\N	7	3	2	7	7	3	0	4	0	4	1	\N	0	0	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	4	4	4	0	2018-11-08	7
365	449	5	0	1	2	4	6	0	0	0	1	4	4	1	2	4	2	3	0	0	5	1	1	0	3	1	0	0	1	1	1	1	5	1	1	1	\N	1	1	0	0	0	6	0	0	1	0	1	3	0	1	1	0	{0,3,4}	4	1	1	1	0	2	5	0	0	0	1	5	2	1	3	3	0	1	5	4	4	3	6	1	1	3	3	0	2	1	1	6	3	5	6	3	5	5	7	5	2	3	5	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	7	0	2	5	5	4	0	2	1	0	0	7	0	0	0	\N	1	1	2	0	0	7	4	2	4	1	0	3	0	1	0	0	0	0	2	0	0	1	1	2018-11-08	3
366	452	3	0	1	3	3	3	0	0	2	3	1	1	0	1	3	0	1	0	0	0	4	0	0	1	0	1	1	2	0	0	0	\N	0	1	1	\N	2	2	0	0	1	6	0	0	1	\N	4	3	0	1	1	1	{0,3,4}	1	1	1	0	4	0	4	0	0	0	1	0	0	1	1	1	0	1	8	1	0	1	8	3	0	2	8	0	1	0	1	8	1	1	8	4	0	0	3	4	1	1	3	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	0	\N	1	2	2	1	0	6	0	0	0	1	6	1	0	0	0	6	0	0	0	1	0	3	0	1	\N	\N	\N	\N	1	1	4	0	3	2018-11-08	0
367	455	5	0	1	2	1	6	0	2	3	3	0	2	0	1	3	2	0	0	0	1	5	4	4	1	1	0	0	1	2	0	0	9	1	1	1	\N	4	0	0	0	1	12	1	\N	3	\N	4	1	2	1	0	1	{7}	0	1	1	1	0	0	5	5	0	0	2	3	0	0	0	5	0	0	5	2	0	0	6	0	6	3	0	0	1	0	5	5	5	4	6	6	0	3	6	2	1	0	2	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	5	2	3	7	0	0	0	0	4	0	4	0	0	0	0	0	1	3	1	0	7	1	1	5	0	0	3	0	1	\N	\N	\N	\N	3	0	2	0	0	2018-11-08	0
368	457	4	1	2	4	0	\N	1	0	2	3	2	4	0	2	4	1	0	0	0	4	1	2	0	1	1	1	0	0	0	0	0	\N	1	1	1	\N	1	1	0	0	0	4	0	0	1	\N	1	3	0	1	1	1	{3}	6	1	1	1	4	0	4	0	0	3	2	8	0	2	0	0	0	0	1	1	0	0	7	0	0	1	1	0	0	1	0	1	0	0	3	3	0	3	4	1	1	1	1	1	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	1	3	3	1	1	1	7	2	1	\N	0	\N	\N	\N	\N	0	0	0	0	7	0	0	0	0	0	3	0	1	\N	\N	\N	\N	0	1	4	1	0	2028-11-08	2
369	460	4	0	0	1	0	\N	1	1	1	3	3	4	1	2	5	2	3	0	0	5	0	0	0	3	0	\N	1	0	0	0	0	\N	0	1	1	\N	1	1	1	0	0	6	0	0	1	\N	0	2	0	1	1	1	{4}	7	1	1	1	0	2	0	5	0	2	0	3	2	1	0	3	0	1	3	3	1	0	2	2	1	1	1	0	1	1	1	2	3	3	3	3	2	4	3	1	1	0	1	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	2	\N	\N	0	1	1	0	1	\N	0	\N	\N	\N	0	0	0	0	1	\N	\N	\N	\N	\N	0	2	0	1	\N	\N	\N	\N	5	0	\N	\N	\N	2018-11-08	0
370	462	3	0	1	2	1	\N	1	1	1	2	2	3	1	4	4	1	0	0	0	4	0	0	0	1	0	1	1	0	0	0	0	4	0	1	1	\N	1	1	1	0	0	12	0	0	1	\N	3	3	1	1	1	1	{0}	7	1	1	1	5	2	0	0	0	4	0	1	1	0	1	0	0	0	1	0	0	0	5	0	1	1	0	0	1	0	0	2	1	4	5	2	0	5	3	1	1	1	4	0	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	2	0	0	0	0	1	1	1	1	\N	\N	\N	\N	0	0	1	0	0	\N	\N	\N	\N	\N	0	0	0	0	1	\N	\N	\N	\N	0	0	3	1	2	2018-11-08	0
371	464	4	1	0	3	0	6	1	0	1	3	4	4	0	3	3	1	2	0	0	4	5	1	0	2	0	1	1	0	0	0	0	1	0	1	1	\N	1	1	0	0	0	6	0	0	2	\N	1	2	0	1	1	1	{4}	6	0	0	\N	5	2	0	0	0	4	1	1	1	0	0	0	0	0	4	0	0	0	6	0	0	0	0	0	1	0	0	0	1	0	1	3	0	4	3	1	1	0	1	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	1	0	0	6	0	0	5	2	1	\N	\N	\N	\N	\N	\N	0	0	0	0	6	0	0	0	0	0	3	0	1	\N	\N	\N	\N	0	0	4	0	1	2018-11-08	0
372	467	4	0	0	2	2	6	1	0	2	1	4	1	0	2	1	1	3	0	0	3	5	1	2	1	2	1	1	3	0	0	0	\N	1	1	1	\N	1	1	0	3	1	6	0	0	0	\N	3	2	0	1	1	1	{5}	6	1	\N	1	0	0	0	3	0	0	0	0	0	0	1	2	0	1	3	3	1	0	5	1	0	0	2	1	2	3	1	6	1	0	0	2	0	1	3	3	1	1	3	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	3	0	\N	0	2	2	2	0	6	2	1	2	3	2	0	4	3	0	6	0	0	0	3	0	3	0	0	7	1	1	0	2	0	3	0	0	2018-11-08	0
373	469	4	0	0	4	0	\N	1	0	2	3	2	2	0	3	4	1	1	0	\N	5	5	0	0	3	\N	1	1	0	0	0	1	8	0	1	1	\N	1	1	0	0	0	4	0	0	0	\N	1	2	0	1	1	1	{4}	0	1	1	1	0	0	0	4	0	0	0	6	6	3	3	1	0	2	6	3	3	3	6	1	2	6	5	0	6	2	1	3	1	1	1	3	0	6	4	5	1	2	2	2	1	\N	\N	\N	\N	0	{}	\N	\N	1	0	2	1	1	0	0	1	4	2	1	\N	\N	\N	\N	\N	0	0	4	2	0	5	0	0	0	0	0	0	0	1	\N	0	0	\N	1	0	4	1	1	2018-11-08	1
374	473	4	0	0	2	0	\N	1	0	1	3	4	4	1	4	3	1	3	0	0	5	0	0	0	3	0	1	1	0	0	0	0	\N	1	1	0	\N	2	3	0	10	2	\N	0	0	2	0	3	3	0	1	1	1	{0}	6	1	1	1	0	4	0	0	0	2	0	6	6	0	0	5	0	1	1	0	0	0	6	0	0	2	2	0	1	1	0	2	1	5	5	0	0	0	7	1	1	1	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	2	4	0	\N	0	1	3	4	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	0	\N	\N	\N	5	0	1	\N	\N	\N	\N	5	0	3	1	3	2018-11-08	0
375	472	4	1	1	\N	0	\N	1	0	1	3	3	4	0	4	3	1	0	\N	1	3	5	3	2	2	0	1	1	0	2	0	2	9	1	1	1	\N	1	1	1	\N	\N	\N	0	0	0	\N	1	1	0	1	1	1	{4}	4	1	1	0	2	0	0	1	0	2	0	6	1	4	3	1	1	2	3	6	1	1	6	2	0	7	3	1	1	2	0	6	6	3	3	3	2	2	3	3	1	1	2	2	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	3	2	2	0	1	3	6	1	\N	\N	\N	\N	0	0	0	1	1	0	4	1	1	6	\N	0	2	0	1	\N	\N	\N	\N	\N	\N	4	4	2	2018-11-08	1
376	474	4	0	0	4	0	\N	1	1	0	1	2	2	0	4	5	1	3	0	0	4	0	0	0	2	0	1	1	0	0	0	7	8	1	1	1	\N	0	1	0	2	0	12	0	1	1	\N	1	1	0	1	1	1	{0}	6	1	\N	1	0	0	0	0	0	0	0	5	3	0	0	4	0	1	1	4	0	3	6	0	0	3	0	1	0	1	0	2	3	4	3	2	0	3	2	0	1	0	1	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	2	1	3	0	\N	0	2	0	2	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	0	\N	\N	\N	\N	\N	0	1	\N	\N	0	0	0	0	4	0	3	2018-11-08	0
377	475	4	0	4	2	0	\N	1	0	2	3	3	4	1	4	4	1	2	0	2	2	0	1	2	2	0	1	1	0	1	0	2	5	1	1	1	\N	1	1	0	0	0	6	0	0	3	\N	3	1	2	1	1	1	{4}	5	1	1	1	0	2	4	0	0	4	0	5	5	0	0	5	1	2	5	3	1	0	5	3	6	3	2	1	0	2	0	2	1	6	5	6	3	5	1	2	1	2	4	2	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	4	3	6	0	2	1	5	1	11	0	\N	\N	1	6	0	0	0	0	2	2	2	6	1	0	3	0	1	\N	0	0	0	0	\N	1	0	1	0218-11-08	0
378	476	4	0	2	1	3	1	0	2	2	3	4	2	1	\N	5	0	2	0	0	1	0	0	1	2	1	1	1	1	0	0	0	8	2	1	0	\N	2	1	0	1	0	5	0	0	1	0	3	2	1	1	0	0	{3,4}	6	0	0	1	4	0	0	0	1	0	0	0	2	2	2	2	0	3	8	3	0	1	8	1	2	8	3	0	1	2	3	8	8	6	0	1	0	8	4	7	1	3	8	2	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	1	0	2	1	0	2	3	1	0	5	0	0	1	1	0	0	1	0	0	3	0	0	0	1	0	3	0	0	6	0	0	0	3	0	3	1	4	2018-11-08	0
379	477	4	0	2	3	0	4	1	1	2	3	3	4	1	3	4	2	0	0	0	4	5	0	0	2	0	1	1	0	4	0	0	8	1	1	1	\N	2	1	1	0	0	12	0	0	0	\N	4	3	3	0	1	1	{3,4}	5	1	\N	1	4	2	2	4	1	4	0	5	5	1	1	2	0	1	3	1	1	3	2	1	0	0	0	1	0	1	1	3	0	5	5	3	0	1	4	2	0	0	2	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	2	3	1	0	2	6	3	0	8	0	0	0	1	6	1	1	0	0	8	0	0	0	1	0	2	0	1	\N	\N	\N	\N	\N	\N	3	0	0	2018-11-08	0
380	461	4	0	0	2	0	6	0	1	2	3	1	2	0	4	4	0	3	0	0	3	4	0	3	1	0	1	1	0	1	0	2	1	1	1	1	\N	1	1	0	0	0	6	0	0	2	\N	1	2	0	1	1	1	{0,3,4,5}	\N	0	0	0	0	2	0	0	0	0	0	5	0	5	2	0	0	2	5	5	3	0	6	3	2	6	6	1	\N	6	6	1	0	6	6	7	1	7	3	3	4	4	7	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	5	5	4	0	2	0	5	1	\N	\N	\N	\N	2	2	0	2	0	0	5	2	5	4	1	0	2	0	1	\N	0	0	0	2	0	3	0	0	2004-01-21	0
381	468	3	0	1	1	1	6	0	0	0	3	3	1	0	1	3	1	0	0	0	4	4	0	0	2	0	1	1	0	0	0	0	\N	2	1	1	\N	2	1	1	\N	2	\N	0	0	2	\N	2	3	0	1	1	1	{0,3}	1	0	0	0	4	2	0	4	0	3	1	2	1	2	2	3	0	8	4	3	1	5	8	3	1	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	7	4	3	3	3	1	6	1	2	0	\N	\N	\N	\N	1	{}	\N	\N	7	6	2	7	3	3	0	2	1	2	1	\N	\N	\N	\N	0	\N	0	1	0	1	\N	\N	\N	\N	\N	\N	\N	0	1	\N	\N	\N	\N	\N	0	3	3	2	2018-11-08	4
382	451	4	1	1	2	3	6	1	0	2	3	3	3	1	4	5	0	0	0	0	5	5	0	1	1	0	1	1	2	0	0	7	6	1	0	1	0	2	4	0	6	0	6	0	0	0	\N	1	2	1	1	1	1	{4}	7	0	0	0	0	2	4	4	0	0	0	5	5	6	5	2	1	3	4	3	5	5	6	5	5	0	5	1	3	5	1	7	5	8	5	5	0	5	1	6	2	2	8	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	1	2	6	4	0	2	2	1	1	\N	\N	\N	\N	0	0	1	4	0	0	6	1	2	6	0	0	1	0	1	\N	0	0	0	0	4	2	1	2	2004-02-12	2
383	478	4	1	0	1	0	\N	0	0	0	3	3	4	1	4	4	1	0	0	0	3	5	1	1	3	0	1	0	0	1	0	0	5	1	1	1	\N	1	0	1	\N	\N	\N	1	\N	0	\N	1	2	3	1	1	1	{4}	7	1	1	1	0	2	0	0	0	0	0	1	0	0	0	1	0	0	6	1	0	1	6	0	1	6	6	0	1	0	0	6	1	5	6	7	1	6	4	5	1	0	6	5	\N	\N	\N	\N	\N	1	{}	\N	\N	6	1	2	3	7	3	0	4	2	3	1	\N	\N	\N	\N	0	0	0	4	1	0	3	1	2	6	1	0	3	0	1	\N	\N	\N	\N	\N	\N	4	1	0	2018-11-08	0
384	453	3	0	3	1	0	\N	1	1	3	2	2	4	0	1	3	0	3	1	0	5	5	1	1	2	0	0	1	1	1	0	0	8	0	1	1	\N	1	2	1	9	0	12	0	0	2	\N	3	3	0	1	1	1	{0,3,4,7}	4	1	1	1	0	2	0	4	1	1	0	5	1	1	1	2	1	1	1	0	0	0	5	4	3	2	5	1	3	3	0	5	0	0	0	2	1	1	3	5	1	1	5	1	\N	\N	\N	\N	\N	0	{}	\N	\N	6	1	2	5	5	3	0	1	0	7	0	7	0	4	0	2	2	0	1	2	0	3	2	6	4	4	0	3	0	1	\N	\N	\N	\N	2	0	3	0	0	2018-11-08	0
385	479	5	1	0	2	0	2	1	1	1	2	4	3	1	4	5	0	3	0	0	5	0	0	0	1	0	1	1	0	1	2	2	2	0	1	1	\N	1	1	0	1	0	5	1	1	1	\N	0	2	0	1	1	1	{3,4}	7	1	1	0	0	2	0	0	0	0	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	1	0	4	3	2	6	0	2	2	3	1	\N	0	0	0	1	\N	1	4	0	1	\N	0	0	0	0	0	1	1	1	\N	0	0	0	5	0	0	2	4	2018-10-01	2
386	483	4	0	0	\N	0	6	0	1	1	3	3	4	0	4	5	0	3	1	0	2	1	1	2	2	0	1	1	0	2	1	7	9	2	1	1	\N	2	3	1	0	0	12	0	0	0	\N	0	1	2	1	1	1	{4}	1	1	1	0	0	2	0	4	0	4	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	7	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	1	1	4	1	2	5	0	1	6	4	1	\N	0	0	0	0	\N	1	4	2	0	7	0	2	\N	1	1	4	0	\N	\N	0	0	0	3	0	2	3	1	2018-10-01	5
387	481	4	1	3	1	4	6	0	1	1	3	1	4	0	0	4	1	3	0	0	1	3	2	2	2	0	0	0	0	6	2	4	6	1	1	1	4	2	3	0	5	0	2	0	0	0	\N	0	2	0	1	1	1	{0,3,6}	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	7	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	\N	\N	\N	6	0	3	6	7	0	5	1	1	2	0	6	0	4	0	0	3	1	5	1	2	2	3	0	0	5	1	0	0	3	3	0	0	0	2018-10-01	5
388	484	4	1	2	2	1	6	0	0	2	2	2	3	1	3	4	0	3	1	0	2	5	2	1	2	0	1	1	0	1	2	7	0	2	1	1	5	1	1	0	0	0	2	0	0	0	\N	1	1	0	1	0	0	{3,4,5}	1	1	\N	1	2	2	2	1	0	0	1	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	4	0	2	2	0	1	1	2	0	7	0	0	0	0	6	1	2	0	0	3	1	4	7	1	0	3	0	1	\N	0	0	0	1	1	3	2	2	2018-10-01	2
389	487	4	0	0	2	3	6	1	0	1	1	4	3	1	3	5	1	2	0	0	3	0	0	0	3	0	1	1	0	0	0	7	9	0	1	1	\N	1	1	0	2	2	\N	0	0	0	\N	1	1	3	1	1	1	{0,4,5}	2	1	\N	1	0	0	4	5	0	3	0	0	0	1	4	3	0	1	1	3	0	2	5	2	0	0	6	0	1	2	0	6	1	5	5	8	0	6	7	1	1	2	6	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	0	4	1	0	2	2	3	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	1	0	0	0	2	2018-11-09	1
390	488	3	1	0	1	0	4	0	0	2	3	4	4	1	3	5	1	0	3	0	2	0	0	0	1	0	1	1	0	0	0	7	8	0	1	1	\N	2	2	1	7	0	9	0	0	0	\N	1	3	1	0	0	1	{4}	3	0	0	0	5	2	0	0	2	4	0	6	6	3	5	7	0	6	6	3	1	7	6	7	4	5	5	1	5	2	0	8	0	5	5	5	5	5	1	5	1	3	5	5	1	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	4	2	0	0	4	8	8	0	8	3	1	2	5	3	1	4	0	0	7	6	6	3	4	2	3	0	0	7	0	1	0	3	4	4	0	0	2018-11-09	1
391	489	3	0	2	3	1	6	1	0	2	3	2	4	1	3	4	1	3	0	0	3	2	3	0	2	0	1	1	1	2	0	7	8	1	1	1	\N	1	1	1	\N	2	\N	0	1	1	\N	1	2	2	0	1	1	{6}	6	1	1	1	3	1	0	2	0	1	0	6	7	1	3	3	0	1	2	8	3	3	6	5	3	8	8	0	3	4	6	4	3	6	8	0	3	7	4	3	4	8	6	6	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	5	7	6	0	3	2	8	1	\N	\N	\N	\N	2	8	0	1	0	0	5	2	4	4	1	0	2	0	1	\N	\N	\N	\N	1	\N	2	1	2	2018-11-09	4
392	490	3	0	1	1	2	1	1	0	1	3	3	4	1	4	5	1	1	0	0	5	0	0	1	1	0	1	1	0	0	0	7	8	1	1	1	\N	1	0	0	0	0	6	0	0	1	\N	1	2	3	1	1	1	{4}	3	1	1	1	0	2	0	2	0	4	0	1	3	3	3	6	0	3	3	2	4	1	4	2	3	2	2	0	5	1	1	4	3	3	3	4	2	4	4	3	2	2	7	2	\N	\N	\N	\N	\N	1	{}	\N	\N	5	1	2	6	4	5	1	2	9	3	1	\N	\N	\N	\N	1	0	0	0	0	1	\N	0	\N	\N	\N	\N	5	0	1	\N	\N	\N	\N	0	0	3	1	3	2018-11-09	4
393	491	3	0	0	2	0	\N	1	1	1	0	3	4	0	4	3	1	0	0	0	3	5	0	0	3	0	1	1	0	0	0	0	\N	\N	1	1	\N	0	1	0	9	2	\N	0	1	0	\N	0	1	0	1	1	1	{0,4}	3	1	\N	1	4	2	0	5	0	3	0	5	5	1	1	0	0	1	1	6	1	0	3	1	3	3	0	0	0	0	0	5	1	3	5	3	0	0	4	0	0	0	0	0	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	0	0	\N	1	1	1	8	1	\N	0	0	0	0	0	0	0	0	1	\N	0	0	0	0	0	0	0	1	\N	0	0	0	0	0	4	1	3	2018-11-09	0
394	493	4	0	0	3	1	\N	1	0	2	3	2	2	0	3	2	1	2	0	0	0	4	3	2	2	0	1	1	0	0	0	2	1	1	1	1	\N	1	2	0	1	0	6	0	1	0	\N	1	1	2	1	1	1	{0,3,4}	5	1	1	1	0	2	0	0	0	1	0	3	3	3	3	4	0	3	4	4	2	3	6	3	1	3	3	0	1	1	1	6	1	3	1	6	1	4	3	2	1	1	6	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	3	0	\N	0	1	2	2	0	3	2	4	0	3	2	0	2	0	0	3	2	3	1	2	1	2	0	1	\N	\N	\N	\N	0	0	2	0	0	2018-11-09	1
395	492	2	1	0	3	2	1	0	3	3	3	3	3	1	2	4	1	0	0	2	3	5	0	0	2	3	1	1	4	3	2	0	\N	0	1	1	\N	2	1	0	0	0	11	0	0	1	\N	2	2	0	1	1	1	{1,5,7}	0	1	1	1	4	2	4	0	0	3	3	1	8	0	\N	1	1	4	4	1	1	0	6	6	2	7	2	0	2	3	0	1	1	3	1	3	3	7	2	5	3	6	8	0	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	0	2	0	0	\N	1	1	6	5	1	\N	0	0	2	1	0	1	0	0	1	\N	0	0	0	0	0	1	0	1	\N	0	0	0	0	\N	1	0	\N	2018-11-09	0
396	494	4	0	0	3	1	\N	1	1	1	3	3	3	0	3	3	1	0	1	0	4	0	0	0	1	0	1	1	0	0	0	7	1	1	1	1	\N	2	0	0	1	2	12	0	0	1	\N	1	2	0	1	1	1	{0,3,4}	6	1	1	1	0	2	4	0	0	1	0	0	0	1	1	1	0	0	2	3	1	0	1	1	0	4	2	0	1	1	2	2	2	0	0	6	1	5	4	1	1	0	5	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	2	3	0	\N	0	3	1	4	1	\N	\N	\N	\N	1	\N	0	3	1	0	5	0	0	0	0	0	2	0	1	\N	\N	\N	\N	0	0	4	0	0	2018-11-09	0
397	495	3	0	0	2	4	6	0	3	0	0	4	4	0	4	5	1	3	0	0	5	5	4	0	2	0	1	1	0	0	0	2	7	2	1	1	\N	1	1	0	2	0	4	0	0	0	\N	0	2	0	1	1	1	{4}	4	0	0	1	0	2	0	0	0	3	2	0	1	1	1	0	0	1	3	5	1	1	5	2	1	5	2	0	4	2	\N	1	0	1	5	2	0	1	8	2	1	1	5	5	\N	\N	\N	\N	\N	0	{}	\N	\N	0	1	2	6	3	6	1	2	6	5	1	\N	\N	\N	\N	0	0	0	0	0	0	8	2	2	7	0	0	2	0	1	\N	0	0	0	1	1	4	1	0	2018-11-09	2
398	496	4	0	0	1	1	\N	1	1	1	3	4	4	0	4	5	1	3	5	0	5	5	1	0	2	0	1	1	0	0	0	0	\N	\N	1	0	\N	0	1	0	9	0	4	0	0	0	1	1	2	3	1	1	1	{3,4,5}	6	0	0	1	0	3	0	2	0	3	0	3	3	0	7	1	0	3	6	4	0	0	8	3	1	0	7	0	7	4	6	7	0	7	4	7	3	3	4	8	2	3	8	2	\N	\N	\N	\N	\N	0	{}	\N	\N	1	0	2	5	3	6	0	0	2	6	1	\N	\N	\N	\N	\N	\N	0	4	\N	0	1	0	0	0	0	0	3	0	1	\N	0	0	0	1	0	4	2	1	2018-11-09	2
399	497	3	1	1	0	3	6	0	3	0	3	3	4	1	2	4	2	1	0	0	0	\N	0	0	1	0	1	1	2	0	0	1	5	0	0	1	1	0	2	0	3	0	0	0	1	1	\N	3	1	2	1	1	1	{2,6,7}	7	1	1	0	0	1	2	2	0	4	0	1	1	0	0	4	0	4	3	6	0	0	4	2	1	1	3	0	1	3	0	8	0	3	5	1	0	7	8	5	2	3	6	1	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	2	6	1	3	0	2	3	5	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	0	0	1	\N	0	0	0	5	0	4	1	2	2018-11-09	2
400	499	3	0	0	3	0	\N	1	0	2	3	4	4	1	4	4	1	3	0	0	3	5	4	4	3	0	1	1	0	0	0	1	7	2	1	1	\N	1	1	0	0	0	2	0	0	0	\N	2	3	1	1	1	1	{4}	1	0	0	1	4	2	0	5	0	3	0	0	1	1	3	5	0	2	5	2	1	6	1	2	1	4	4	0	4	4	1	5	2	5	6	3	2	4	3	7	3	3	8	2	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	5	6	6	0	4	1	1	0	6	3	1	2	5	6	0	3	0	0	3	3	6	1	3	0	3	0	0	8	4	0	0	1	0	4	0	0	2018-11-09	7
401	498	4	0	1	1	3	3	0	0	3	1	3	4	1	4	4	2	0	0	5	5	3	1	1	2	0	1	0	1	1	0	6	9	1	1	1	\N	2	0	0	0	0	3	0	0	0	\N	3	0	2	1	1	1	{4,7}	6	1	1	1	0	2	5	5	0	4	0	6	6	1	1	3	0	5	1	4	0	3	4	1	1	3	4	0	2	2	0	8	2	5	0	6	1	6	4	0	1	1	3	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	0	0	\N	1	1	1	8	0	6	0	0	0	0	0	0	4	3	0	6	1	2	4	1	2	3	0	0	6	0	0	0	3	0	2	0	0	2018-11-09	0
402	501	4	0	1	3	0	\N	1	1	2	3	4	4	1	3	4	1	0	0	0	5	0	0	0	2	0	1	1	0	0	0	0	9	0	1	1	\N	0	1	0	0	0	4	0	0	1	\N	0	1	0	1	1	1	{3,4}	6	1	\N	1	0	0	0	4	0	3	0	6	6	0	0	1	0	3	1	6	0	0	5	0	0	3	0	0	1	1	1	3	0	3	5	3	0	0	3	1	2	2	3	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	0	\N	0	1	1	7	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	0	\N	2	0	1	\N	\N	\N	\N	0	0	4	0	1	2018-11-09	0
403	502	4	0	1	3	1	6	1	0	2	2	3	4	1	3	2	0	1	0	0	5	0	0	0	1	0	1	1	0	0	0	2	9	1	1	1	\N	2	2	0	0	0	12	0	1	1	\N	1	2	1	1	1	1	{4}	6	1	\N	1	3	0	4	4	0	4	0	3	3	0	1	2	0	1	1	3	0	0	5	1	0	5	2	0	1	2	0	5	1	3	1	1	0	5	4	2	1	1	1	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	5	0	\N	0	1	0	4	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	1	0	\N	\N	\N	\N	\N	\N	\N	4	0	3	2018-11-09	0
404	500	4	0	0	4	0	\N	1	0	0	3	3	4	1	3	4	1	0	0	0	5	0	0	0	2	0	1	1	0	0	0	0	\N	0	1	1	\N	0	0	0	1	0	6	0	0	1	\N	1	1	0	1	1	1	{0,3,4}	6	1	\N	1	0	2	0	5	0	3	0	6	6	0	6	1	0	1	1	5	1	0	5	1	1	5	5	0	1	1	5	7	0	5	5	6	0	6	4	1	1	1	6	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	0	\N	0	0	1	7	1	\N	\N	\N	\N	\N	0	0	0	0	1	\N	\N	0	\N	0	0	2	0	1	\N	\N	\N	\N	0	0	4	0	2	2018-11-09	0
405	503	3	0	3	2	2	6	0	0	2	3	1	4	1	4	3	1	3	0	0	4	0	0	0	2	0	1	1	0	0	0	0	9	1	1	1	\N	2	1	0	0	0	12	0	1	1	\N	3	3	0	1	1	1	{4}	4	1	1	1	0	0	0	5	0	2	0	0	6	0	0	1	0	1	0	1	1	1	2	0	0	6	1	0	0	0	0	7	2	6	6	6	0	3	8	3	0	0	5	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	1	0	\N	0	1	2	6	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	0	0	2	0	1	\N	0	0	0	0	0	4	1	1	2018-11-09	0
406	504	3	0	0	2	1	6	1	0	1	3	1	4	1	1	5	0	0	0	0	5	0	0	2	1	0	1	1	1	0	0	0	8	0	1	1	\N	2	1	0	5	2	\N	0	0	3	\N	3	3	0	1	1	1	{4}	7	0	0	1	4	2	3	0	2	1	0	0	0	0	0	0	0	0	0	5	0	0	3	0	0	0	0	0	3	0	0	2	0	0	2	2	0	2	3	5	0	5	0	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	2	0	0	1	0	1	0	7	1	4	0	2	6	1	4	0	0	5	1	2	7	1	0	3	0	1	\N	\N	\N	\N	1	0	4	0	1	2018-11-09	0
407	505	3	0	1	1	0	\N	1	1	1	3	4	4	1	3	4	1	1	0	0	2	5	0	0	2	0	0	1	0	0	0	0	8	0	1	1	\N	1	2	1	9	1	12	0	0	0	\N	1	3	1	1	1	1	{4}	7	0	0	1	0	2	0	0	0	3	0	0	0	0	0	1	0	0	0	0	0	0	5	1	2	0	1	0	3	0	0	1	2	5	5	1	2	1	2	1	1	1	7	0	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	\N	2	5	0	0	0	1	5	0	0	6	0	0	0	1	6	0	1	0	0	5	0	0	0	0	0	3	0	1	\N	\N	\N	\N	1	\N	3	2	1	2018-11-09	0
408	506	4	0	3	3	0	\N	1	0	2	3	3	4	1	3	3	1	3	0	0	4	0	0	2	1	0	1	1	0	0	0	0	\N	1	1	1	\N	1	1	0	2	2	\N	0	1	1	\N	1	2	0	1	1	1	{3}	6	1	\N	1	4	0	4	0	0	4	0	\N	1	1	1	1	0	1	1	1	0	1	2	2	1	2	2	1	2	1	0	5	1	2	1	1	1	3	1	2	1	1	1	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	5	0	\N	0	1	5	4	0	6	0	7	0	1	0	0	4	4	0	\N	1	3	4	\N	0	3	0	0	\N	0	0	0	2	\N	4	0	2	2018-11-09	0
409	507	4	0	0	4	0	\N	1	1	0	3	2	4	1	4	5	1	3	0	0	5	5	4	0	2	0	1	1	0	0	1	7	9	2	1	1	\N	0	0	1	\N	2	\N	0	0	1	\N	1	2	0	1	1	1	{0,4}	6	0	0	1	0	2	1	4	0	4	0	6	5	1	3	3	0	3	3	1	3	0	2	2	1	3	3	1	3	2	1	5	1	3	0	3	1	1	2	0	1	2	1	1	\N	\N	\N	\N	\N	1	{}	\N	\N	6	2	2	5	2	3	0	4	7	8	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	\N	\N	5	0	1	\N	\N	\N	\N	\N	0	4	0	4	2018-11-09	6
410	509	4	0	1	3	0	6	0	1	1	3	3	4	1	4	5	1	3	0	0	2	4	1	2	2	0	1	0	0	0	0	0	8	1	1	1	\N	0	0	0	9	2	6	0	1	1	\N	1	1	0	1	1	1	{6}	6	1	1	1	0	2	0	1	0	3	0	6	6	1	5	2	0	1	2	1	1	1	2	3	1	2	2	1	2	2	1	8	1	5	5	2	1	3	3	5	2	2	5	2	\N	\N	\N	\N	\N	0	{}	\N	\N	3	0	2	2	0	0	0	2	6	8	0	7	0	0	2	2	3	0	2	4	0	6	1	2	4	1	0	3	0	1	11	0	0	0	3	0	2	0	3	2018-11-09	0
411	508	4	0	0	1	3	6	1	0	4	1	1	2	0	1	4	1	3	0	2	2	5	1	0	0	2	1	0	7	3	3	7	9	0	0	1	2	2	0	0	0	0	3	0	0	0	\N	0	1	2	1	1	1	{0}	7	0	1	1	4	2	4	4	0	3	2	8	8	0	0	0	0	0	0	1	0	2	3	0	0	3	0	1	0	0	0	8	1	3	0	3	2	3	5	2	0	0	0	0	0	\N	\N	\N	\N	0	{}	\N	\N	7	3	2	4	5	4	0	2	2	0	0	7	0	4	0	3	6	0	2	0	0	6	4	6	1	2	0	3	0	0	7	0	0	0	1	0	3	0	0	2018-11-09	4
412	511	4	0	0	3	1	6	1	0	2	2	2	2	0	2	4	1	0	0	0	4	5	0	2	1	0	1	1	0	0	0	0	\N	1	1	1	\N	0	1	0	0	0	12	0	0	1	\N	1	2	3	1	1	1	{0,3,4}	6	1	1	1	0	0	0	5	0	3	0	6	1	0	0	1	0	1	1	3	0	0	5	0	0	3	0	0	0	0	0	5	0	3	3	2	0	3	3	0	0	1	0	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	5	0	\N	0	1	0	2	1	\N	\N	\N	\N	0	0	0	0	0	\N	1	\N	\N	\N	\N	\N	1	0	1	\N	\N	\N	\N	\N	0	4	0	4	2018-11-09	\N
413	510	4	1	0	2	1	2	1	0	2	3	2	4	1	1	4	1	0	0	0	5	5	0	0	3	0	1	1	0	0	0	0	\N	0	1	1	\N	0	0	1	\N	0	6	0	0	1	\N	3	3	1	1	1	1	{0,3,4,6}	7	1	\N	1	4	2	0	0	0	1	2	5	5	0	1	1	0	5	2	2	0	0	5	5	2	5	5	1	5	2	1	5	2	2	5	5	0	2	1	5	1	2	5	1	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	1	0	\N	0	2	4	6	1	\N	\N	\N	\N	\N	\N	0	4	0	1	\N	\N	\N	\N	0	1	1	0	1	\N	\N	\N	\N	2	0	4	0	0	2018-11-09	0
414	512	3	0	4	0	4	6	0	0	4	3	4	4	1	4	5	1	0	0	0	5	5	4	3	2	0	\N	0	0	0	1	3	0	0	1	1	\N	0	1	0	5	0	0	0	0	0	1	3	3	1	0	0	1	{3}	7	1	\N	0	5	2	0	0	0	4	2	0	1	1	1	0	0	1	2	0	1	0	3	0	2	1	1	0	1	1	1	1	1	1	0	8	0	1	4	8	1	1	6	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	0	6	0	0	2	9	1	0	3	0	3	1	2	2	0	1	0	0	1	1	1	1	4	0	4	0	0	6	0	1	0	4	0	1	0	0	2018-11-09	4
415	514	4	0	3	2	0	\N	0	1	1	3	1	4	1	4	4	1	3	0	0	5	0	0	2	1	0	1	1	0	0	0	2	9	0	1	1	\N	0	1	\N	9	2	\N	0	0	1	\N	1	1	0	1	1	1	{3}	7	1	\N	1	0	0	0	0	0	3	2	3	0	0	2	0	0	3	3	0	0	0	6	3	0	6	1	0	3	0	1	8	0	0	4	6	0	3	3	5	2	0	5	0	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	6	0	\N	0	1	2	6	1	\N	\N	\N	\N	\N	\N	0	1	0	1	\N	\N	\N	\N	0	0	4	0	1	\N	\N	\N	\N	2	0	4	0	1	2018-11-09	0
416	513	3	0	0	4	0	3	1	1	4	3	4	4	1	4	3	1	0	0	0	3	5	0	0	1	0	1	1	1	0	0	0	8	0	1	1	\N	2	1	0	1	0	6	0	0	1	\N	1	2	3	1	1	1	{6,7}	5	1	\N	1	4	2	0	0	2	2	0	0	4	5	6	0	0	0	5	0	2	6	5	3	3	2	4	0	2	0	0	5	4	0	0	4	0	4	2	5	0	1	6	0	\N	\N	\N	\N	\N	1	{}	\N	\N	5	3	2	3	0	\N	0	1	0	4	0	7	0	0	0	0	0	0	0	0	0	3	1	4	4	1	0	4	0	1	\N	0	0	0	1	0	2	2	2	2018-11-09	1
417	515	1	1	1	1	0	\N	1	0	0	2	2	4	0	4	4	1	0	0	0	3	0	0	0	1	0	1	1	0	0	0	0	\N	\N	1	1	\N	2	0	1	0	0	\N	0	1	3	\N	4	1	0	1	1	0	{3}	7	1	1	1	0	2	0	4	0	3	0	1	7	2	7	2	0	3	0	4	1	4	4	4	2	4	1	\N	2	0	0	0	1	1	0	1	1	1	1	2	0	1	1	1	\N	\N	\N	\N	\N	1	{}	\N	\N	5	0	2	2	0	2	0	0	4	6	0	0	0	0	0	1	6	0	\N	0	1	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	3	0	1	2018-11-09	0
418	516	4	0	1	1	3	6	1	0	1	2	4	4	0	4	4	0	3	0	0	5	5	1	0	1	0	1	1	0	0	0	0	8	1	1	1	\N	0	0	0	0	0	5	0	1	0	\N	1	3	1	1	1	1	{6}	6	1	\N	1	0	2	0	4	0	3	0	0	0	0	3	6	0	2	4	3	1	1	6	1	3	3	3	0	1	2	1	6	3	5	5	5	0	6	3	5	2	2	5	1	\N	\N	\N	\N	\N	1	{}	\N	\N	4	0	2	5	2	4	0	2	4	0	1	\N	\N	\N	\N	0	0	0	0	0	1	\N	\N	\N	\N	\N	\N	2	0	1	\N	\N	\N	\N	5	0	4	3	2	2018-11-09	1
419	517	4	0	0	4	2	6	1	0	1	3	4	4	1	4	5	1	1	0	0	5	0	0	0	1	0	1	1	0	1	0	0	9	0	1	1	\N	2	0	1	0	0	6	0	0	1	\N	1	2	0	1	1	1	{6}	1	0	0	1	0	2	4	4	0	3	0	3	3	1	1	2	0	2	2	0	0	0	6	2	2	2	4	0	4	3	0	8	0	6	3	2	3	3	3	8	4	1	6	4	\N	\N	\N	\N	\N	1	{}	\N	\N	0	6	2	5	4	3	0	2	1	0	1	\N	0	0	0	1	0	1	1	0	0	7	0	0	0	0	0	3	0	1	\N	\N	\N	\N	\N	\N	4	4	1	2018-11-09	1
420	518	4	0	0	2	1	\N	1	1	2	3	4	4	1	4	5	1	1	0	0	3	3	4	1	2	0	1	1	0	0	0	0	8	1	1	1	\N	0	1	1	1	0	6	0	0	0	\N	0	2	0	1	1	1	{3,4}	6	1	\N	1	0	0	0	5	0	3	0	3	4	4	4	1	0	4	4	4	2	0	4	1	3	0	4	0	1	1	0	8	1	3	0	8	0	8	4	8	1	3	8	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	2	0	\N	0	1	9	8	1	\N	\N	\N	\N	1	0	0	1	0	1	\N	0	0	0	\N	0	2	0	1	\N	0	0	0	0	\N	0	0	4	2018-11-09	0
421	519	3	0	1	4	1	6	1	1	2	3	4	4	1	4	3	0	1	0	0	4	5	4	2	1	0	1	1	0	0	0	0	5	0	1	1	\N	2	1	1	1	2	\N	0	1	0	\N	0	1	0	0	1	1	{0}	7	1	1	1	5	2	0	0	0	3	0	0	0	5	5	0	0	2	6	2	5	5	5	5	2	2	6	0	6	7	2	8	2	6	2	6	2	8	4	7	4	8	8	6	0	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	2	1	0	\N	0	2	3	2	1	\N	0	0	0	1	0	0	0	0	0	3	0	0	0	0	1	4	0	1	\N	0	0	0	5	1	4	2	4	2018-11-09	1
422	520	4	0	0	3	0	\N	1	1	0	3	2	2	1	3	3	2	0	0	0	5	0	0	3	3	0	1	1	0	0	0	0	\N	0	1	1	\N	0	1	0	0	0	6	0	0	1	\N	1	2	0	1	1	1	{3,4}	6	1	\N	1	0	0	0	0	0	1	0	1	1	1	3	1	0	2	1	8	5	0	5	1	2	5	2	0	1	2	2	5	1	5	5	5	0	2	4	1	1	2	6	1	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	3	0	\N	0	2	2	6	1	\N	\N	\N	\N	\N	\N	0	0	0	1	\N	\N	\N	\N	0	0	2	0	1	\N	\N	\N	\N	0	0	4	0	2	2018-11-09	0
423	522	5	0	0	2	2	6	0	0	1	3	2	4	1	3	3	1	3	0	0	5	0	4	0	2	0	0	0	0	2	0	5	3	2	1	1	\N	0	0	1	5	2	\N	0	1	2	\N	1	2	2	1	1	1	{}	7	1	1	1	5	2	3	0	0	3	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	\N	0	\N	4	0	1	1	8	1	\N	0	0	1	0	\N	0	0	0	1	0	0	0	0	0	0	5	0	1	\N	0	0	0	5	0	0	0	3	2018-10-17	0
425	525	1	0	0	2	1	6	1	1	2	2	4	4	1	3	4	1	2	0	0	5	0	1	0	1	0	1	1	0	0	0	7	5	0	1	1	\N	2	1	0	0	0	0	0	0	0	\N	3	3	1	1	\N	1	{4}	5	1	1	1	0	3	0	4	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	\N	6	2	6	0	4	1	4	1	\N	0	0	0	2	\N	0	1	0	0	7	1	1	7	0	0	3	0	\N	\N	0	0	0	0	0	3	0	4	2018-10-18	6
426	526	1	0	0	1	\N	1	1	1	3	3	1	4	1	4	\N	1	1	\N	1	5	2	0	\N	1	0	1	1	0	0	1	2	9	0	1	1	\N	1	0	0	0	0	6	0	0	1	\N	0	2	0	1	1	1	{3}	3	1	1	1	0	2	0	3	0	0	3	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	0	2	4	0	6	0	2	9	4	1	\N	\N	\N	\N	0	\N	0	3	0	1	\N	0	\N	\N	0	0	0	1	1	\N	0	0	0	0	0	0	0	0	2018-10-17	0
427	527	5	0	0	1	1	6	1	0	1	3	1	1	1	1	5	1	1	0	0	2	2	2	0	2	1	1	0	0	0	0	0	\N	0	1	1	\N	0	0	0	0	0	6	0	0	1	\N	1	2	3	1	1	1	{}	7	1	1	1	5	2	0	0	0	3	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	\N	4	\N	\N	0	1	0	0	1	\N	0	0	0	2	6	0	1	4	1	\N	0	0	0	0	0	3	0	1	\N	0	0	0	1	1	1	1	1	2018-10-02	2
428	528	3	0	2	0	3	6	1	0	2	2	2	4	1	2	3	0	2	0	0	2	0	0	0	4	0	1	1	0	0	0	0	\N	1	1	1	\N	2	1	0	2	0	6	0	0	0	\N	2	3	1	1	1	1	{4,5}	1	1	1	1	4	2	0	0	0	3	0	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	9	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	0	0	1	0	0	1	1	7	1	\N	0	0	0	0	\N	0	0	0	1	\N	0	0	0	0	0	2	0	1	0	0	0	0	5	0	\N	1	0	2018-10-17	0
429	529	4	0	0	3	3	6	1	0	2	3	1	4	1	2	4	0	2	0	0	5	0	0	2	2	0	1	1	0	0	0	7	9	1	1	1	\N	1	2	0	2	0	6	0	0	1	\N	2	2	1	1	1	1	{}	6	1	1	1	4	2	0	0	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	2	0	0	0	2	0	4	1	\N	0	0	0	\N	0	0	0	0	1	\N	0	0	0	0	0	3	0	1	\N	0	0	0	2	0	4	0	2	2018-10-17	0
430	530	5	0	2	1	2	2	1	0	2	1	1	3	1	2	3	1	2	0	0	2	0	0	2	1	2	1	0	5	0	2	0	5	0	1	1	\N	1	1	0	5	0	4	0	0	2	\N	2	1	0	1	1	1	{}	7	1	1	1	4	2	5	0	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	\N	4	\N	\N	0	1	1	2	1	\N	0	0	0	0	\N	1	2	1	1	0	0	0	0	0	0	3	0	1	\N	0	0	0	2	0	4	0	0	2018-10-02	0
431	531	3	0	0	2	1	2	1	0	1	3	4	4	1	2	4	1	3	0	0	5	0	4	2	4	0	1	1	2	0	0	0	7	0	0	0	4	1	3	0	9	1	12	0	0	1	\N	1	3	0	1	1	1	{4}	6	0	0	1	0	2	0	2	0	3	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	1	0	\N	3	2	0	1	6	5	1	\N	0	0	0	0	\N	0	1	0	0	7	3	3	7	3	0	2	0	1	\N	0	0	0	1	0	1	2	1	2018-10-17	2
432	532	2	0	0	0	0	3	1	1	0	3	1	4	0	2	5	1	3	0	0	1	5	2	2	2	0	1	1	0	1	2	2	0	2	1	1	\N	0	1	1	0	0	4	1	1	2	\N	3	1	2	1	1	1	{0}	4	1	1	1	0	0	5	4	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	3	3	2	5	0	4	2	2	1	\N	0	0	0	0	\N	0	4	0	0	0	2	1	8	0	0	2	0	1	\N	0	0	0	3	0	0	1	0	2018-10-17	7
433	533	2	1	1	2	0	6	1	1	2	3	4	4	0	4	4	2	3	0	0	0	0	0	0	2	0	1	0	2	0	0	0	\N	1	0	1	0	2	1	0	2	2	\N	0	1	1	\N	3	2	2	1	1	0	{}	5	1	1	1	4	2	0	0	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	2	3	\N	2	\N	0	1	2	5	5	1	0	0	0	0	0	\N	0	1	0	1	0	0	0	0	0	0	1	0	1	\N	0	0	0	1	0	1	1	1	2018-10-02	1
434	536	5	0	1	0	3	2	0	0	2	2	1	4	1	1	5	0	3	0	0	5	0	1	4	2	3	0	0	7	4	2	1	2	2	1	1	\N	2	3	0	0	0	0	0	0	3	\N	4	4	1	1	1	1	{3}	7	1	1	1	0	1	5	4	0	3	3	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	0	\N	2	2	0	2	6	7	1	\N	0	0	1	0	\N	0	2	2	0	1	1	2	6	1	0	4	0	1	\N	0	0	0	1	0	1	0	2	2018-10-17	0
435	535	4	0	2	1	2	3	0	1	0	1	1	1	1	1	2	0	0	0	0	5	0	0	0	2	0	1	1	0	0	0	0	\N	0	1	1	\N	1	0	0	9	2	\N	0	0	1	0	2	2	0	1	1	1	{0}	1	1	1	0	0	0	0	0	0	1	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	1	1	0	\N	1	1	4	3	1	0	0	0	1	\N	0	0	0	0	0	1	0	0	0	1	1	1	0	1	\N	0	0	0	0	0	4	1	2	2018-11-07	0
436	534	3	0	2	0	3	6	1	0	3	3	0	4	0	3	0	0	3	0	0	5	0	0	2	3	0	1	1	1	0	0	2	9	1	1	1	\N	1	1	0	2	0	4	0	0	0	\N	3	3	0	1	1	1	{3,4}	5	1	1	1	5	0	0	4	0	3	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	\N	\N	\N	\N	\N	0	0	2	0	8	1	\N	0	0	0	1	\N	0	4	1	0	8	1	1	7	0	1	4	0	1	\N	0	0	0	5	0	\N	0	2	2018-10-17	2
437	537	3	0	0	2	4	6	1	0	2	2	4	4	1	3	4	1	2	0	0	5	0	0	1	3	0	1	1	0	0	0	0	\N	1	1	1	\N	0	1	0	1	0	6	0	0	1	\N	2	2	0	1	1	1	{0,3,4,5}	6	1	1	1	0	0	0	5	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	\N	0	\N	\N	0	1	0	0	1	\N	0	0	0	0	\N	0	0	0	1	\N	0	0	0	0	0	2	0	1	\N	0	0	0	1	0	0	3	3	2018-10-17	0
438	538	1	0	0	2	2	6	0	0	0	3	2	4	1	2	3	2	3	0	0	4	0	0	2	1	1	0	0	0	1	0	0	2	2	1	1	\N	0	1	1	0	0	2	0	0	0	\N	0	2	1	1	1	1	{3}	4	1	1	1	0	4	0	4	0	4	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	3	2	3	3	6	0	3	9	8	1	\N	0	0	0	0	\N	1	1	0	1	\N	0	0	0	0	0	5	0	1	\N	0	0	0	5	0	4	0	0	2018-10-17	3
439	539	4	1	0	1	0	\N	1	1	3	3	3	4	1	2	2	1	0	0	0	0	0	0	0	2	0	1	1	0	0	0	1	8	0	1	1	\N	1	4	1	9	2	\N	0	0	2	\N	2	1	0	1	1	1	{0}	4	1	1	1	4	0	0	0	0	1	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	1	0	0	\N	0	1	3	5	1	\N	0	0	0	0	\N	1	0	0	1	\N	0	0	0	0	0	0	0	1	\N	0	0	0	0	0	3	0	2	2018-10-17	0
440	542	4	0	0	3	0	\N	1	0	1	3	2	4	1	3	3	1	1	0	0	5	5	0	0	\N	0	1	1	0	1	0	0	\N	1	1	1	\N	0	1	0	6	0	6	0	0	2	\N	1	2	0	1	1	1	{0,3,4,7}	6	1	1	1	0	0	2	0	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	2	2	0	\N	0	1	1	3	1	\N	\N	\N	\N	\N	\N	0	1	1	1	0	0	0	0	0	0	1	0	1	0	0	0	0	1	0	3	0	3	2018-10-17	0
441	540	3	0	2	1	4	6	1	1	0	2	\N	1	1	4	3	0	0	1	1	5	5	4	0	2	0	0	0	1	1	1	7	9	1	1	1	\N	4	2	0	6	0	12	1	1	0	\N	1	0	2	1	1	1	{}	5	1	1	1	0	1	0	0	0	3	1	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	\N	\N	\N	\N	\N	6	1	3	0	2	1	\N	0	0	0	0	\N	0	0	0	1	\N	\N	0	0	0	0	1	1	1	\N	0	0	0	5	2	3	3	0	2018-12-17	1
442	544	5	0	2	1	3	2	1	1	3	1	3	4	1	4	3	0	1	0	0	4	5	2	0	2	0	1	1	0	0	0	0	\N	2	1	1	\N	0	1	0	5	1	12	0	0	2	\N	3	2	1	1	1	1	{}	4	1	1	1	4	2	0	0	\N	4	2	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	{}	\N	\N	0	\N	\N	0	\N	0	0	2	1	4	1	\N	0	0	0	0	\N	1	0	0	1	\N	0	0	0	0	0	3	0	1	\N	0	0	0	0	0	4	1	1	2018-10-17	0
443	546	3	0	1	1	2	6	0	0	1	0	0	3	0	4	3	0	3	0	0	4	5	2	0	2	0	1	1	0	0	0	0	\N	2	1	1	\N	1	1	0	1	0	12	1	1	0	\N	2	2	0	1	1	1	{3}	4	1	1	1	1	0	0	0	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	0	\N	2	5	0	\N	0	2	7	5	1	\N	0	0	0	2	5	0	0	0	0	6	2	5	4	2	1	3	0	1	\N	0	0	0	5	1	1	0	3	2018-11-07	0
444	545	4	0	0	3	3	6	1	0	3	3	2	4	0	4	3	1	3	0	0	5	5	0	0	3	0	1	1	0	1	3	2	9	1	1	1	\N	3	4	0	0	0	0	0	0	2	\N	2	3	0	1	1	1	{2}	3	1	1	1	5	0	4	0	0	3	0	\N	\N	\N	\N	\N	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	3	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0	{}	\N	\N	5	0	2	2	0	\N	0	1	2	2	1	\N	0	0	0	0	\N	0	0	0	0	6	0	0	0	1	0	3	0	1	\N	0	0	0	2	0	3	0	1	2003-06-01	1
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add Ação	7	add_acao
26	Can change Ação	7	change_acao
27	Can delete Ação	7	delete_acao
28	Can view Ação	7	view_acao
29	Can add aluno	8	add_aluno
30	Can change aluno	8	change_aluno
31	Can delete aluno	8	delete_aluno
32	Can view aluno	8	view_aluno
33	Can add campanha	9	add_campanha
34	Can change campanha	9	change_campanha
35	Can delete campanha	9	delete_campanha
36	Can view campanha	9	view_campanha
37	Can add escola	10	add_escola
38	Can change escola	10	change_escola
39	Can delete escola	10	delete_escola
40	Can view escola	10	view_escola
41	Can add exame	11	add_exame
42	Can change exame	11	change_exame
43	Can delete exame	11	delete_exame
44	Can view exame	11	view_exame
45	Can add Questionário	12	add_questionario
46	Can change Questionário	12	change_questionario
47	Can delete Questionário	12	delete_questionario
48	Can view Questionário	12	view_questionario
49	Can add diretor	13	add_diretor
50	Can change diretor	13	change_diretor
51	Can delete diretor	13	delete_diretor
52	Can view diretor	13	view_diretor
53	Can add Token	14	add_token
54	Can change Token	14	change_token
55	Can delete Token	14	delete_token
56	Can view Token	14	view_token
57	Can add documento	15	add_documento
58	Can change documento	15	change_documento
59	Can delete documento	15	delete_documento
60	Can view documento	15	view_documento
61	Can add foto	16	add_foto
62	Can change foto	16	change_foto
63	Can delete foto	16	delete_foto
64	Can view foto	16	view_foto
65	Can add noticia	17	add_noticia
66	Can change noticia	17	change_noticia
67	Can delete noticia	17	delete_noticia
68	Can view noticia	17	view_noticia
69	Can add video	18	add_video
70	Can change video	18	change_video
71	Can delete video	18	delete_video
72	Can view video	18	view_video
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$120000$A2iMGoWxb28G$ukQzEG1KULRkLCdoIUPwn2OsChWaHhMmjn+OWSeySAc=	2019-01-03 01:04:26.176008+00	t	sadoadmin				t	t	2018-11-12 04:25:10.762311+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
985fb94499ccb5ef727672289ebc0c2fe1480616	2018-11-12 04:25:10.957923+00	1
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2018-11-12 12:08:54.651913+00	1	Pesquisa sobre saúde bucal da rede municipal de ensino de Palmas	1	[{"added": {}}]	9	1
2	2018-11-12 12:09:11.1335+00	1	Pesquisa	1	[{"added": {}}]	7	1
3	2018-11-12 12:12:47.702733+00	1	Escola municipal Luiz Gonzaga	1	[{"added": {}}]	10	1
4	2018-11-12 16:58:26.624519+00	1	Levantamento epidemiológico	2	[{"changed": {"fields": ["nome"]}}]	7	1
5	2018-11-12 17:03:54.474227+00	2	Escola municipal Mestre Pacífico S. Campos	1	[{"added": {}}]	10	1
6	2018-11-12 17:08:13.416667+00	3	Escola municipal Beatriz Rodrigues da Silva	1	[{"added": {}}]	10	1
7	2018-11-12 17:09:08.641589+00	4	Escola municipal de T.I. Padre Josimo M. Tavares	1	[{"added": {}}]	10	1
8	2018-11-12 17:09:44.212106+00	5	Escola municipal Anne Frank	1	[{"added": {}}]	10	1
9	2018-11-12 17:10:15.129885+00	6	Escola municipal Henrique Talone Pinheiro	1	[{"added": {}}]	10	1
10	2018-11-12 17:11:02.736966+00	7	Escola municipal Antônio Carlos Jobim	1	[{"added": {}}]	10	1
11	2018-11-12 17:11:37.033013+00	8	Escola municipal Aurélio Buarque de Holanda	1	[{"added": {}}]	10	1
12	2018-11-12 17:23:48.903488+00	9	Escola Silverio Ribeiro Matos	1	[{"added": {}}]	10	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	administracao	acao
8	administracao	aluno
9	administracao	campanha
10	administracao	escola
11	administracao	exame
12	administracao	questionario
13	administracao	diretor
14	authtoken	token
15	gerencia	documento
16	gerencia	foto
17	gerencia	noticia
18	gerencia	video
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-11-12 04:21:14.618599+00
2	auth	0001_initial	2018-11-12 04:21:14.737161+00
3	admin	0001_initial	2018-11-12 04:21:14.778633+00
4	admin	0002_logentry_remove_auto_add	2018-11-12 04:21:14.793659+00
5	admin	0003_logentry_add_action_flag_choices	2018-11-12 04:21:14.811191+00
6	administracao	0001_initial	2018-11-12 04:21:15.157346+00
7	administracao	0002_auto_20180830_1527	2018-11-12 04:21:15.204214+00
8	administracao	0003_auto_20180830_1728	2018-11-12 04:21:15.228719+00
9	administracao	0004_auto_20180831_1437	2018-11-12 04:21:15.29378+00
10	administracao	0005_auto_20180831_1605	2018-11-12 04:21:15.305043+00
11	administracao	0006_auto_20180831_1751	2018-11-12 04:21:15.348065+00
12	administracao	0007_auto_20180904_1045	2018-11-12 04:21:15.446905+00
13	administracao	0008_auto_20181111_2341	2018-11-12 04:21:22.762754+00
14	contenttypes	0002_remove_content_type_name	2018-11-12 04:21:22.932022+00
15	auth	0002_alter_permission_name_max_length	2018-11-12 04:21:22.950645+00
16	auth	0003_alter_user_email_max_length	2018-11-12 04:21:22.974075+00
17	auth	0004_alter_user_username_opts	2018-11-12 04:21:22.991505+00
18	auth	0005_alter_user_last_login_null	2018-11-12 04:21:23.012912+00
19	auth	0006_require_contenttypes_0002	2018-11-12 04:21:23.019471+00
20	auth	0007_alter_validators_add_error_messages	2018-11-12 04:21:23.038098+00
21	auth	0008_alter_user_username_max_length	2018-11-12 04:21:23.063682+00
22	auth	0009_alter_user_last_name_max_length	2018-11-12 04:21:23.085755+00
23	authtoken	0001_initial	2018-11-12 04:21:23.119877+00
24	authtoken	0002_auto_20160226_1747	2018-11-12 04:21:23.233075+00
25	sessions	0001_initial	2018-11-12 04:21:23.264522+00
26	administracao	0009_auto_20181112_0903	2018-11-12 12:34:20.082621+00
27	administracao	0010_auto_20181112_0924	2018-11-12 12:34:20.36803+00
28	administracao	0011_auto_20181112_1413	2018-11-12 18:32:24.654296+00
29	administracao	0012_remove_aluno_numero_identificacao	2018-11-12 18:32:24.724547+00
30	administracao	0013_aluno_numero_identificacao	2018-11-15 11:10:56.000233+00
31	administracao	0014_auto_20181112_1617	2018-11-15 11:10:56.132211+00
32	administracao	0015_auto_20181114_2309	2018-11-15 11:11:02.398273+00
33	administracao	0016_auto_20181115_0054	2018-11-15 11:11:03.264+00
34	administracao	0017_auto_20181115_0946	2018-11-15 12:54:20.748964+00
35	administracao	0018_auto_20181115_1003	2018-11-15 13:16:15.952141+00
36	administracao	0019_auto_20181115_1012	2018-11-15 13:16:17.098113+00
37	administracao	0020_questionario_questao_69	2018-11-15 13:37:12.594112+00
70	administracao	0021_auto_20181115_1412	2018-11-15 17:36:55.202275+00
71	administracao	0022_auto_20181115_1435	2018-11-15 17:36:55.438472+00
72	administracao	0023_auto_20181115_1602	2018-11-16 00:10:20.25882+00
73	administracao	0024_auto_20181115_2058	2018-11-16 00:10:22.505729+00
74	administracao	0025_auto_20181121_1038	2018-11-26 03:34:35.426085+00
75	administracao	0026_auto_20181124_1553	2018-11-26 03:34:36.58999+00
76	administracao	0027_auto_20181124_1601	2018-11-26 03:34:36.616567+00
77	administracao	0028_auto_20181125_2252	2018-11-26 03:34:36.656503+00
78	administracao	0029_auto_20181126_0004	2018-11-26 03:34:36.968338+00
79	gerencia	0001_initial	2018-12-20 05:29:55.431148+00
80	gerencia	0002_auto_20181220_0226	2018-12-20 05:29:55.457203+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
2mm6cqf7729y52mdqv5i0u61w0f47t7t	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-19 11:39:29.7536+00
grqx1paptlftl5g0i6apofw6dk7ra74b	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-20 12:01:44.593757+00
gp8d5ehqnn80no2rdxntfyr1d9kj0fu3	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-24 12:48:26.358706+00
ozfouerrs9fsx6h5fjz6h5oljm145qbd	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-11-30 00:11:37.541544+00
h895njysvx8j7o40pluttsdvk1d5g80d	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-11-30 13:02:33.870341+00
2svm6noe4bnnbtmlr98o8rlbieh6kc7h	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-25 21:05:45.71498+00
vbqtscun6k5nuhi90tnzgmb3u1xyw72t	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-27 14:35:29.791452+00
ti1xxtdi3cf3re8b88eudd4uj4eke83t	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-27 23:49:42.262505+00
166r4hcdfss8xkwfawpkn87v9dr36syd	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2019-01-01 07:37:34.486254+00
44w51az1rrhphd9yiplsghx6g4mlbqmv	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-07 18:05:48.404615+00
1f4d66bwx9qbdrws87qqjx15itpzro6h	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-08 12:15:08.124445+00
50hdtj7nkm4dzwl0tplq5448cdb3tuor	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-08 12:53:10.493118+00
83kj74phfyzcdqfd440trlgpzzznm5xg	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-08 12:57:27.908703+00
0kj9sg8s71pa1gy8xp6gkekpv1knabty	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-08 19:06:41.352494+00
xawv6jcaza1c9o2s5bwgl02kjczvjkmc	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-09 11:57:13.658746+00
zsh5f11nvg4rtxmo0qzsk672nvn77h47	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-09 12:06:02.065668+00
tb9eqd1fb6q7yazncf1ae2qng7g8wgq3	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2019-01-02 22:53:46.897976+00
tlmmfhvvswzus3f3ma0r94bm0hnm2uxn	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-17 23:16:02.859084+00
fks2h7i4bj9ymitpxkd5u973j80faga3	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-18 00:28:53.855523+00
jfy0xjrnfukuy4r7jmdcdp9s5y04ys6h	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2019-01-03 14:09:38.402541+00
a9hectobew0qyjv9w5s5sz5mlycypp7q	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2018-12-18 01:05:10.717227+00
uhi2474aungzp7tnyljdqygafgjgu5r9	OGNiNWNmZTEzYjgzMjQ0ODVlNzY0NGNmMWM3MGZiMzNkMjEwNGE5OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNTQ4ZWQ5ZTM1ZGFlMWI1ZDA0MzBjYjRhZTNhZDgyOWVmOWE3NWI4In0=	2019-01-17 01:04:26.184387+00
\.


--
-- Data for Name: gerencia_documento; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.gerencia_documento (id, titulo, data, url) FROM stdin;
1	Questionários.pdf	2018-12-20 05:32:45.42546+00	https://drive.google.com/uc?id=1Fivn1UBrXB3PX55UfWBrfrTldoVabQWb
2	Projeto de pesquisa.pdf	2018-12-20 05:33:14.282209+00	https://drive.google.com/uc?id=11_jQq-FViIDPOGhtxrEz969sWNEDUW2h
3	Anexos.pdf	2018-12-20 06:30:50.722907+00	https://drive.google.com/uc?id=13WNaFdfs6WS6WBBPvmuFVmj1X_ead1Ki
\.


--
-- Data for Name: gerencia_foto; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.gerencia_foto (id, titulo, data, url) FROM stdin;
1	Reunião com os diretores	2018-12-20 05:52:36.852423+00	https://imgur.com/bGdZH8o.jpg
2	Reunião com os diretores	2018-12-20 05:52:56.77201+00	https://imgur.com/rXPXupt.jpg
3	Reunião com os diretores	2018-12-20 05:53:17.039793+00	https://imgur.com/O64S1Us.jpg
4	Coleta de dados	2018-12-20 05:53:38.374804+00	https://imgur.com/eLtFX8M.jpg
5	Coleta de dados	2018-12-20 05:53:54.853681+00	https://imgur.com/ivuhyw6.jpg
6	Coleta de dados	2018-12-20 05:54:12.62346+00	https://imgur.com/PK2nkP3.jpg
7	Coleta de dados	2018-12-20 05:54:32.457244+00	https://imgur.com/jK77Ox4.jpg
8	Coleta de dados	2018-12-20 05:54:53.563471+00	https://imgur.com/W2thO1L.jpg
9	Registro de dados	2018-12-20 05:55:21.808051+00	https://imgur.com/X7x4XJw.jpg
10	Registro de dados	2018-12-20 05:55:37.070314+00	https://imgur.com/qB3ItWy.jpg
11	Registro de dados	2018-12-20 05:55:54.444415+00	https://imgur.com/Y5crRLZ.jpg
12	Registro de dados	2018-12-20 05:56:09.908006+00	https://imgur.com/RrWMfvr.jpg
\.


--
-- Data for Name: gerencia_noticia; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.gerencia_noticia (id, titulo, data, texto, imagem) FROM stdin;
1	Reunião com os diretores de colégio	08 de Junho de 2018 às 09:56	Ao longo dos últimos dias seguiram-se várias reuniões entre o professor Nilton Vale Cavalcante e os diretores das escolas públicas municipais da cidade de Palmas. Seu objetivo foi buscar apoio para que possa realizar a pesquisa sobre saúde bucal na rede básica de ensino, de modo que possa ter dados amostrais de qualidade sobre esta população.	https://imgur.com/O64S1Us.jpg
2	Projeto piloto	08 de Agosto de 2018 às 18:11	Neste dia foi iniciado o projeto piloto na Escola Municipal Luiz Gonzaga, na zona norte de Palmas. Serão coletados os dados de exame bucal e questionário de sete crianças do 9º ano do ensino fundamental, justamente o público-alvo da pesquisa.\r\n\r\nApós a coleta dos dados haverá um processamento das informações para verificar se existem erros no sistema e gerar as primeiras conclusões a respeito do que foi coletado.	https://imgur.com/eLtFX8M.jpg
3	Início da coleta definitiva de dados	29 de Agosto de 2018 às 11:45	Com o término da fase piloto e a resolução de algumas deficiências encontradas no sistema, iniciou-se a coleta definitiva dos dados. Ao todo participaram oito escolas da rede de pública municipal de ensino de Palmas:\r\n\r\nEscola municipal Mestre Pacífico S. Campos;\r\nEscola municipal Luiz Gonzaga;\r\nEscola municipal Beatriz Rodrigues da Silva;\r\nEscola municipal Anne Frank;\r\nEscola municipal Henrique Talone Pinheiro;\r\nEscola municipal de T.I. Padre Josimo M. Tavares;\r\nEscola municipal Antônio Carlos Jobim; e\r\nEscola municipal de T.I. Margarida Gonçalves.\r\n\r\nAo longo das próximas semanas é esperada a coleta de dados de pouco menos de 500 alunos, totalizando um número amostral suficiente para que sejam realizados estudos e análises.	https://imgur.com/jK77Ox4.jpg
\.


--
-- Data for Name: gerencia_video; Type: TABLE DATA; Schema: public; Owner: pxopsbpdrfglvt
--

COPY public.gerencia_video (id, titulo, data, url) FROM stdin;
1	Conversa com os alunos 1	2018-12-20 05:41:23.82566+00	https://www.youtube.com/embed/JXCoNPdk9Ec
2	Conversa com os alunos 2	2018-12-20 05:41:43.298745+00	https://www.youtube.com/embed/3CA4mKBU_N8
\.


--
-- Name: administracao_acao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.administracao_acao_id_seq', 68, true);


--
-- Name: administracao_aluno_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.administracao_aluno_id_seq', 579, true);


--
-- Name: administracao_campanha_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.administracao_campanha_id_seq', 1, true);


--
-- Name: administracao_diretor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.administracao_diretor_id_seq', 8, true);


--
-- Name: administracao_escola_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.administracao_escola_id_seq', 43, true);


--
-- Name: administracao_exame_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.administracao_exame_id_seq', 472, true);


--
-- Name: administracao_questionario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.administracao_questionario_id_seq', 477, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 72, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 12, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 18, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 80, true);


--
-- Name: gerencia_documento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.gerencia_documento_id_seq', 3, true);


--
-- Name: gerencia_foto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.gerencia_foto_id_seq', 12, true);


--
-- Name: gerencia_noticia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.gerencia_noticia_id_seq', 3, true);


--
-- Name: gerencia_video_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pxopsbpdrfglvt
--

SELECT pg_catalog.setval('public.gerencia_video_id_seq', 2, true);


--
-- Name: administracao_acao administracao_acao_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_acao
    ADD CONSTRAINT administracao_acao_pkey PRIMARY KEY (id);


--
-- Name: administracao_aluno administracao_aluno_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_aluno
    ADD CONSTRAINT administracao_aluno_pkey PRIMARY KEY (id);


--
-- Name: administracao_campanha administracao_campanha_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_campanha
    ADD CONSTRAINT administracao_campanha_pkey PRIMARY KEY (id);


--
-- Name: administracao_diretor administracao_diretor_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_diretor
    ADD CONSTRAINT administracao_diretor_pkey PRIMARY KEY (id);


--
-- Name: administracao_escola administracao_escola_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_escola
    ADD CONSTRAINT administracao_escola_pkey PRIMARY KEY (id);


--
-- Name: administracao_exame administracao_exame_aluno_id_key; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_exame
    ADD CONSTRAINT administracao_exame_aluno_id_key UNIQUE (aluno_id);


--
-- Name: administracao_exame administracao_exame_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_exame
    ADD CONSTRAINT administracao_exame_pkey PRIMARY KEY (id);


--
-- Name: administracao_questionario administracao_questionario_aluno_id_key; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_questionario
    ADD CONSTRAINT administracao_questionario_aluno_id_key UNIQUE (aluno_id);


--
-- Name: administracao_questionario administracao_questionario_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_questionario
    ADD CONSTRAINT administracao_questionario_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: gerencia_documento gerencia_documento_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.gerencia_documento
    ADD CONSTRAINT gerencia_documento_pkey PRIMARY KEY (id);


--
-- Name: gerencia_foto gerencia_foto_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.gerencia_foto
    ADD CONSTRAINT gerencia_foto_pkey PRIMARY KEY (id);


--
-- Name: gerencia_noticia gerencia_noticia_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.gerencia_noticia
    ADD CONSTRAINT gerencia_noticia_pkey PRIMARY KEY (id);


--
-- Name: gerencia_video gerencia_video_pkey; Type: CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.gerencia_video
    ADD CONSTRAINT gerencia_video_pkey PRIMARY KEY (id);


--
-- Name: administracao_acao_campanha_id_0b5cc6d0; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX administracao_acao_campanha_id_0b5cc6d0 ON public.administracao_acao USING btree (campanha_id);


--
-- Name: administracao_aluno_escola_id_8033f123; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX administracao_aluno_escola_id_8033f123 ON public.administracao_aluno USING btree (escola_id);


--
-- Name: administracao_diretor_escola_id_1f26cf6c; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX administracao_diretor_escola_id_1f26cf6c ON public.administracao_diretor USING btree (escola_id);


--
-- Name: administracao_escola_acao_id_f36775a3; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX administracao_escola_acao_id_f36775a3 ON public.administracao_escola USING btree (acao_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: pxopsbpdrfglvt
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: administracao_acao administracao_acao_campanha_id_0b5cc6d0_fk_administr; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_acao
    ADD CONSTRAINT administracao_acao_campanha_id_0b5cc6d0_fk_administr FOREIGN KEY (campanha_id) REFERENCES public.administracao_campanha(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: administracao_aluno administracao_aluno_escola_id_8033f123_fk_administr; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_aluno
    ADD CONSTRAINT administracao_aluno_escola_id_8033f123_fk_administr FOREIGN KEY (escola_id) REFERENCES public.administracao_escola(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: administracao_diretor administracao_direto_escola_id_1f26cf6c_fk_administr; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_diretor
    ADD CONSTRAINT administracao_direto_escola_id_1f26cf6c_fk_administr FOREIGN KEY (escola_id) REFERENCES public.administracao_escola(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: administracao_escola administracao_escola_acao_id_f36775a3_fk_administracao_acao_id; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_escola
    ADD CONSTRAINT administracao_escola_acao_id_f36775a3_fk_administracao_acao_id FOREIGN KEY (acao_id) REFERENCES public.administracao_acao(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: administracao_exame administracao_exame_aluno_id_9d297f20_fk_administracao_aluno_id; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_exame
    ADD CONSTRAINT administracao_exame_aluno_id_9d297f20_fk_administracao_aluno_id FOREIGN KEY (aluno_id) REFERENCES public.administracao_aluno(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: administracao_questionario administracao_questi_aluno_id_a57b8064_fk_administr; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.administracao_questionario
    ADD CONSTRAINT administracao_questi_aluno_id_a57b8064_fk_administr FOREIGN KEY (aluno_id) REFERENCES public.administracao_aluno(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pxopsbpdrfglvt
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pxopsbpdrfglvt
--

REVOKE ALL ON SCHEMA public FROM postgres;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO pxopsbpdrfglvt;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: LANGUAGE plpgsql; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON LANGUAGE plpgsql TO pxopsbpdrfglvt;


--
-- PostgreSQL database dump complete
--

